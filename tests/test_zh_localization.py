"""Red/green tests for the Myspoti localized resource validation."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'tools/check_zh_localization.py'


class LocalizationTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.project = Path(self.tempdir.name)
        folders = [
            'base/app/src/main/res/values-zh',
            'localization',
        ]
        for folder in folders:
            dest = self.project / folder
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(ROOT / folder, dest)
        self.main = self.project / 'base/app/src/main/res/values-zh/myspoti_strings.xml'

    def check(self):
        return subprocess.run([sys.executable, str(SCRIPT), '--project', str(self.project)], text=True, capture_output=True)

    def update_xml(self, regex, replacement):
        text = self.main.read_text(encoding='utf-8')
        updated, count = re.subn(regex, replacement, text, count=1)
        self.assertEqual(count, 1)
        self.main.write_text(updated, encoding='utf-8')

    def test_baseline_passes(self):
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_changed_exact_translation_fails(self):
        self.update_xml(r'(<string name="welcome_login">)[^<]+(</string>)', r'\1Log in with Spotify\2')
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('welcome-login-zh', result.stderr)

    def test_corrupted_printf_fails(self):
        self.update_xml(r'(<string name="settings_crossfade_seconds">)%1\$d', r'\g<1>%1$s')
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('format', result.stderr.lower().replace('placeholders', 'format placeholders'))

    def test_missing_key_fails(self):
        self.update_xml(r'\s*<string name="welcome_login">[^<]+</string>', '')
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('pinned upstream baseline', result.stderr)

    def test_duplicate_key_fails(self):
        self.update_xml(r'</resources>', '<string name="welcome_login">duplicate</string>\n</resources>')
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('duplicate', result.stderr.lower())


if __name__ == '__main__':
    unittest.main()
