# Myspoti 简体中文汉化 · 开发与验证说明

> **已更新为完整中文主页：请优先阅读 [README.md](README.md)**，包括原版完整功能、截图、下载、安装、常见问题、许可及原作者鸣谢。原作者英文介绍另存为 [README.en.md](README.en.md)。

本仓库的**真正汉化源码位于 [i18n/zh-hans](https://github.com/HypnosysNyx/myspoti/tree/i18n/zh-hans) 分支**。上游来源为 [kota-zo/myspoti](https://github.com/kota-zo/myspoti)，代码基线为 `3ab91a0`（2026-10-23）。

汉化资源为 `base/app/src/main/res/values-zh/myspoti_strings.xml`（493 个字符串及 3 组复数）与 `values-zh/strings.xml`（38 个非品牌字符串）。保持品牌、内部数据标识、占位符、Spotify 登录及播放行为不变；Spotify 官网、外部网页与服务端内容不在本地化范围。

## 编译与验证

```bash
git clone --branch i18n/zh-hans https://github.com/HypnosysNyx/myspoti.git
cd myspoti
python3 tools/check_zh_localization.py --project .
python3 -m unittest discover -s tests -p 'test_zh_localization.py'
cd base
./gradlew assembleDebug
```

Windows 中可以使用 `.\gradlew.bat assembleDebug`。需要 JDK 17+ 和 Android SDK（compileSdk 37）。

- [历史汉化 QA 记录](https://github.com/HypnosysNyx/myspoti/blob/i18n/zh-hans/docs/localization-QA-report-zh-CN.md)
- [GitHub Actions 构建结果](https://github.com/HypnosysNyx/myspoti/actions)
- [下载与发布页面](https://github.com/HypnosysNyx/myspoti/releases)

**请以 Releases 是否确实包含 APK 附件、对应提交构建结果和设备测试为准。** 静态检查通过不代表所有机型和界面通过实际验收；使用测试签名的 APK 不保证以后可覆盖升级。使用第三方客户端及广告拦截功能可能违反 Spotify 服务条款。

使用中发现漏译，请向[本仓库 Issues](https://github.com/HypnosysNyx/myspoti/issues)反馈截图、操作路径、版本与设备信息。不要公开个人账号信息或令牌。

## 版权

继承原项目 [GPL-3.0](LICENSE) 及第三方组件的许可证要求。原项目开发者与完整技术致谢请见 [README](README.md)。