# Myspoti 简体中文界面资源补丁

这是针对 `kota-zo/myspoti` 的**非官方简体中文源码补丁**，不包含 APK，也不包含 Spotify 官方程序。仅增加 Android 字符串资源与回归检查文件，不修改 Spotify 播放逻辑、下载逻辑、广告处理逻辑或数据标识符。

## 版本与范围

- 上游仓库：https://github.com/kota-zo/myspoti
- 目标分支：`main`
- 源码基线：`3ab91a07074abd7e23011245b8fa10afc0117b20`（2026-10-23）
- 语言：简体中文，对应 Android 的 `values-zh` / `zh` 语言标签
- 覆盖：`myspoti_strings.xml` 493 条字符串 + 3 组复数；`strings.xml` 38 条字符串。`app_name` 保持原品牌名 Myspoti。
- 上游已自带 `values-zh/spotify_strings.xml` 和 `values-zh/spotify_plurals.xml`，本补丁不会覆盖它们。

## 安装源码补丁

1. 从 GitHub 克隆 `kota-zo/myspoti` 仓库；建议先创建个人工作分支。为了避免上游更新导致资源键变化，可先检出上述固定提交。
2. 将压缩包内的 `base`、`tools`、`localization`、`tests`、`docs` 等目录放到**仓库根目录**，按原路径合并文件；不要用本补丁替换整个 `values-zh` 目录。
3. 在仓库根目录运行：`python tools/check_zh_localization.py --project .`。应检查完整资源、占位符、主要 Kotlin 调用点与回归用例。
4. 安装 JDK 17+、Android SDK（项目要求 compileSdk 37），在 Windows PowerShell 中运行 `cd base`，再运行 `.\gradlew.bat :app:assembleDebug`。也可按上游 README 运行 `./gradlew assembleDebug`。
5. 编译成功后 APK 通常位于 `base/app/build/outputs/apk/debug/`。这一位置以项目实际构建输出为准。测试版和 GitHub 正式 APK 的签名可能不同，不能保证直接覆盖安装；先备份应用内离线数据，避免误卸载造成数据丢失。
6. 打开 Myspoti，进入 **Settings → Display and language → App language → 中文**，或者将设备系统语言设置为简体中文并选择自动语言。

## 验证限制

已经验证资源 XML 可解析、源资源键全集指纹匹配、格式参数保持一致，并准备了登录、设置、下载、歌词、播放器设备和验证流程的回归用例。由于当前工作环境无法克隆完整仓库和运行 Android SDK，**未执行 Gradle 编译、未生成 APK，也未做 Android 设备截图验证**。`check_zh_localization.py` 在完整仓库中会额外检查英文原资源和 Kotlin 渲染路径。

用户提供屏幕截图后，可以按 `localization/regressions-zh-CN.json` 为漏译界面增加新用例。服务端返回的内容、歌曲信息、品牌名、设备名称、用户数据及 Spotify 官方页面不属于本补丁的翻译范围。

## 许可和安全

原项目采用 GPL-3.0；本补丁需遵守原项目许可。它不是官方版本，不应借此推断 Spotify 或设备兼容性已经得到验证。使用可能违反 Spotify 服务条款的功能存在账号风险。
