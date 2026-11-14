#!/usr/bin/env python3
"""Read-only QA for Myspoti Android zh resources. Uses the Python stdlib only."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

RESOURCE_ROOT = Path('base/app/src/main/res')
BASELINE_COMMIT = '3ab91a07074abd7e23011245b8fa10afc0117b20'
FINGERPRINTS = {'myspoti_strings.xml': '1bdae9d4', 'strings.xml': '8f2ac368'}
SOURCE_COUNTS = {'myspoti_strings.xml': 496, 'strings.xml': 39}
FORMATS = re.compile(r'%(?:[1-9][0-9]*\$)?[-#+ 0,(]*\d*(?:\.\d+)?[a-zA-Z%]')


def fingerprint(keys):
    result = 2166136261
    for char in '\n'.join(sorted(keys)):
        result = ((result ^ ord(char)) * 16777619) & 0xffffffff
    return f'{result:08x}'


def load_resources(path):
    root = ET.parse(path).getroot()
    if root.tag != 'resources':
        raise ValueError(f'Not an Android resources file: {path}')
    entries = {}
    for node in root:
        if node.tag not in ('string', 'plurals'):
            raise ValueError(f'Unexpected resource type {node.tag} in {path}')
        name = node.attrib.get('name')
        if not name or name in entries:
            raise ValueError(f'Missing or duplicate key: {name} in {path}')
        if node.tag == 'string':
            if not (node.text or '').strip():
                raise ValueError(f'Empty text for {name}')
            entries[name] = ('string', node.text or '')
        else:
            forms = {}
            for child in node:
                if child.tag != 'item' or 'quantity' not in child.attrib:
                    raise ValueError(f'Invalid plural in {name}')
                q = child.attrib['quantity']
                if q in forms or not (child.text or '').strip():
                    raise ValueError(f'Duplicate or empty plural {name}/{q}')
                forms[q] = child.text or ''
            if 'other' not in forms:
                raise ValueError(f'Missing other plural for {name}')
            entries[name] = ('plurals', forms)
    return entries


def placeholders(s):
    return Counter(FORMATS.findall(s))


def validate(base):
    problems = []
    checks = 0
    zh_dir = base / RESOURCE_ROOT / 'values-zh'
    default_dir = base / RESOURCE_ROOT / 'values'
    for filename in FINGERPRINTS:
        localized = load_resources(zh_dir / filename)
        keys = set(localized)
        if filename == 'strings.xml':
            keys |= {'app_name'}  # The product name deliberately inherits unchanged.
        digest = fingerprint(keys)
        if digest != FINGERPRINTS[filename]:
            problems.append(f'{filename}: keys differ from the pinned upstream baseline (hash {digest})')
        if len(keys) != SOURCE_COUNTS[filename]:
            problems.append(f'{filename}: expected {SOURCE_COUNTS[filename]} keys, got {len(keys)}')
        formats_path = base / 'localization/upstream-formats.json'
        if formats_path.exists():
            fixture = json.loads(formats_path.read_text(encoding='utf-8'))[filename]
            for key, (kind, value) in localized.items():
                expected = fixture.get(key)
                if kind == 'string':
                    actual = placeholders(value)
                    want = Counter(expected or [])
                    if actual != want:
                        problems.append(f'{filename}/{key}: pinned baseline placeholders {dict(want)} != {dict(actual)}')
                else:
                    for quantity, text in value.items():
                        actual = placeholders(text)
                        want = Counter((expected or {}).get(quantity, []))
                        if actual != want:
                            problems.append(f'{filename}/{key}/{quantity}: pinned baseline plural placeholders {dict(want)} != {dict(actual)}')
            print(f'[OK] {filename}: placeholder fixture checked')
        checks += len(localized)
        upstream = default_dir / filename
        if upstream.exists():
            default = load_resources(upstream)
            if set(default) != keys:
                missing = sorted(set(default) - keys - {'app_name'})
                unknown = sorted(keys - set(default))
                problems.append(f'{filename}: untranslated={missing}, unexpected={unknown}')
            for name, (kind, value) in localized.items():
                if name not in default:
                    continue
                orig_kind, orig_val = default[name]
                if kind != orig_kind:
                    problems.append(f'{filename}/{name}: changed type')
                    continue
                if kind == 'string':
                    if placeholders(orig_val) != placeholders(value):
                        problems.append(f'{filename}/{name}: format specifier mismatch {dict(placeholders(orig_val))} != {dict(placeholders(value))}')
                else:
                    for q, text in value.items():
                        if q in orig_val and placeholders(orig_val[q]) != placeholders(text):
                            problems.append(f'{filename}/{name}/{q}: plural format mismatch')
            print(f'[OK] {filename}: checked against English default')
        else:
            print(f'[SKIP] {filename}: English default not present in patch-only folder')
        print(f'[OK] {filename}: {len(localized)} resource names; upstream fingerprint {digest}')
    cases_path = base / 'localization/regressions-zh-CN.json'
    if cases_path.exists():
        cases = json.loads(cases_path.read_text(encoding='utf-8'))['cases']
        all_strings = {}
        for filename in FINGERPRINTS:
            all_strings.update(load_resources(zh_dir / filename))
        for case in cases:
            key = case['key']
            translated = all_strings.get(key)
            if not translated or translated[0] != 'string' or translated[1] != case['expect_translation']:
                problems.append(f'{case["id"]}: translated string changed')
            source_path = base / case['source_file']
            if source_path.exists():
                source = source_path.read_text(encoding='utf-8')
                for expected in case.get('source_contains', []):
                    if expected not in source:
                        problems.append(f'{case["id"]}: producer expression missing: {expected}')
                renderer_path = base / case.get('render_file', case['source_file'])
                renderer = renderer_path.read_text(encoding='utf-8')
                for expected in case.get('render_contains', []):
                    if expected not in renderer:
                        problems.append(f'{case["id"]}: renderer missing: {expected}')
            else:
                print(f'[SKIP] {case["id"]}: Kotlin renderer unavailable in patch-only folder')
            checks += 1
        print(f'[OK] {len(cases)} exact translation regression cases')
    language = base / 'base/app/src/main/java/com/music/spotui/data/AppLanguage.kt'
    if language.exists():
        code = language.read_text(encoding='utf-8')
        if '"zh", "zh-HK", "zh-TW"' not in code or 'AppCompatDelegate.setApplicationLocales' not in code:
            problems.append('AppLanguage.kt: zh tags or locale application path changed')
        else:
            print('[OK] AppLanguage.kt: Simplified Chinese selectable using original locale code')
    else:
        print('[SKIP] AppLanguage.kt not present in patch-only folder')
    if problems:
        print('\nFAIL: ' + str(len(problems)) + ' error(s)', file=sys.stderr)
        for problem in problems:
            print(' - ' + problem, file=sys.stderr)
        return 1
    print(f'PASS: {checks} localized resource/regression checks; no binary or device run')
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--project', type=Path, default=Path('.'))
    args = parser.parse_args()
    try:
        sys.exit(validate(args.project.resolve()))
    except (OSError, ET.ParseError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        sys.exit(1)
