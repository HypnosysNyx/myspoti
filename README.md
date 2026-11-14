# Myspoti · 简体中文汉化版

<p align="center">
  <img alt="Android 10+" src="https://img.shields.io/badge/Android-10%2B-3DDC84?logo=android&logoColor=white">
  <img alt="简体中文社区汉化" src="https://img.shields.io/badge/语言-简体中文-ff6666">
  <a href="https://github.com/HypnosysNyx/myspoti/actions"><img alt="构建状态" src="https://img.shields.io/github/actions/workflow/status/HypnosysNyx/myspoti/android.yml?branch=i18n%2Fzh-hans&label=Android%20CI"></a>
  <a href="LICENSE"><img alt="GPL-3.0" src="https://img.shields.io/github/license/HypnosysNyx/myspoti"></a>
</p>

**Myspoti 是一款面向 Android 的第三方 Spotify 音乐客户端，支持免费账户播放、广告拦截、离线下载与无损音频等功能。本仓库提供基于原项目的非官方简体中文界面汉化。**

> **项目身份与下载说明：**本仓库由社区维护汉化，**不是 Spotify 官方应用，也不是原作者发布的官方中文版**。源项目为 [kota-zo/myspoti](https://github.com/kota-zo/myspoti)。汉化代码在 [`i18n/zh-hans` 分支](https://github.com/HypnosysNyx/myspoti/tree/i18n/zh-hans)，切勿把默认分支的英文资源误当作中文版。**只有 Releases 中实际附带 APK 时，才能直接下载安装；没有 APK 时请使用下方的编译方法。** 不要从不明网站下载“汉化包”。

<p align="center">
  <img src="docs/screenshots/banner.jpg" alt="Myspoti 首页、播放界面、歌手和专辑展示" width="100%">
</p>

<p align="center">
  <a href="https://github.com/HypnosysNyx/myspoti/releases/download/v2.0.2-beta.3-zh.1/myspoti-2.0.2-beta.3-zh.1-android-debug.apk"><b>⬇ 直接下载中文体验 APK</b></a> ·
  <a href="https://github.com/HypnosysNyx/myspoti/releases/tag/v2.0.2-beta.3-zh.1"><b>📦 v2.0.2-beta.3-zh.1 发布页</b></a> ·
  <a href="docs/releases/v2.0.2-beta.3-zh.1.md"><b>📄 中文版发布说明</b></a> ·
  <a href="https://github.com/HypnosysNyx/myspoti/tree/i18n/zh-hans"><b>🀄 汉化源代码</b></a> ·
  <a href="https://github.com/HypnosysNyx/myspoti/issues"><b>🐛 问题反馈</b></a> ·
  <a href="README.en.md"><b>English / 原版 README</b></a>
</p>

## 为什么选择 Myspoti？

### 🚫 免费账户也可使用广告拦截

Myspoti 在 Spotify 自身网页播放器的基础上工作，并尝试从源头阻止音频广告、视频广告、横幅广告与插播。可以自由选歌、跳过歌曲，而不需要 Root 或安装经过修改的 Spotify 官方 APK。**相关功能可能受到 Spotify 的服务条款、账户状态和地区限制，无法保证永久有效。**

### ⬇️ 下载歌曲和播放列表，支持无损音质

可将单曲、专辑、播放列表和「我喜欢的歌曲」下载至应用内，用于无网络播放。支持 **FLAC 无损音频**（有对应音源时可达到 CD 或高解析度规格）及体积较小的 AAC。应用根据 ISRC 从 Tidal 或 Qobuz 等来源寻找相同录音并执行校验；下载前可能需要在设置中完成一次验证。下载的播放列表可与云端列表同步新增内容。

### ✨ Spotify 的常用功能及扩展

包括首页、搜索、音乐库、播放列表、播客、Spotify Connect、Android Auto，以及**逐字滚动歌词、歌词翻译、官方音乐视频、Genius 歌曲含义介绍**等。

## Myspoti 是什么？

Myspoti 是自行安装的 Android 应用。你使用自己的 Spotify 账号，在 Spotify 的登录页面完成认证；Myspoti 不需要你把账号密码提供给汉化维护者。

技术上，官方 Spotify Web Player 负责播放，Myspoti 在外层提供独立界面并控制播放器。在线播放的记录通常可以同步到 Spotify 的播放历史与 Wrapped；**离线下载文件的播放记录不会记入 Spotify Wrapped**，只计入 Myspoti 自身统计。

## 下载与安装

**系统要求：Android 10 或更高版本。**

1. 下载已发布的 [Myspoti v2.0.2-beta.3-zh.1 中文体验 APK](https://github.com/HypnosysNyx/myspoti/releases/download/v2.0.2-beta.3-zh.1/myspoti-2.0.2-beta.3-zh.1-android-debug.apk)（约 100.6 MB），或在[对应 Release](https://github.com/HypnosysNyx/myspoti/releases/tag/v2.0.2-beta.3-zh.1) 的 Assets 中选择 APK。可选：对照 [SHA256SUMS.txt](https://github.com/HypnosysNyx/myspoti/releases/download/v2.0.2-beta.3-zh.1/SHA256SUMS.txt) 校验完整性。**本版采用开发版 Debug 签名，未宣称为正式稳定版**。其他版本以 Releases 中实际存在的 APK 附件为准。
2. 下载 APK，使用 Android 文件管理器打开；第一次安装时系统可能要求允许该来源安装应用。
3. 启动后选择使用 Spotify 登录，并在**设置 → 显示与语言 → 应用语言**选择简体中文，或使用系统简体中文语言。
4. 根据需要设置音质、通知、蓝牙、文件访问等选项。

**安装提醒：**测试版、原版以及不同签名密钥生成的 APK 未必能够互相覆盖更新；不要在备份离线数据前卸载已有版本。GitHub Actions 中的构建产物可能会过期，**不能代替长期有效的 Release 附件**。

## 功能介绍

### 🎧 日常听歌

- 首页、搜索、分类浏览、新歌、个人音乐库与文件夹。
- 歌手、专辑、播放列表和个人资料页。
- 任意选曲、随机播放、智能随机播放、播放队列拖动排序、单曲/列表循环、交叉淡入淡出与睡眠定时器。
- 播客、有声读物及各自的速度控制、15 秒快进/快退和已播放标记。
- Spotify Connect、Jam、蓝牙设备名称、锁屏控件、通知、桌面小组件和 Android Auto。

### 🎤 歌词与音乐视频

- 同步歌词：在歌词来源支持时提供逐字或逐行滚动，支持翻译。
- **Genius 歌曲解读**：可查看歌曲故事，长按特定歌词行了解歌词含义；可按可用服务翻译。
- **官方音乐视频**：可与音乐同步显示、全屏查看，并选择视频原声或保持音乐音轨。

### 👥 播放列表

- 新建、编辑名称、描述及封面；设置公开、私密或协作模式。
- 在列表内搜索 Spotify 歌曲并添加，获取相关建议。
- 协作列表：邀请好友，查看参与者及歌曲添加者。
- 通过 Spotify Code 或链接分享歌曲、专辑、艺人及播放列表。

### 💾 离线与本地音频

- 将单曲、专辑、播放列表和喜欢的歌曲保存为 FLAC 或 AAC；能否取得对应音源取决于第三方服务。
- 下载数据保存在 Myspoti 应用内并加密，下载列表可以持续同步。
- 支持播放设备上的本地音频文件。

### 🎨 其他体验

- 本地保存个人听歌回顾：常听歌曲、艺人与专辑。
- 深色与 AMOLED 纯黑主题、自定义强调色、节省流量与省电模式。
- 原版提供英语、法语、德语、西班牙语、意大利语、葡萄牙语及希腊语；**本分支额外添加简体中文字符串资源**。部分第三方内容或未经过汉化的界面仍可能显示原语言。

## 2.0 相比旧版的更新

源项目 2.0 重建了主要功能，包括：

- 🚀 更快的界面与切歌速度，以及播放器故障自动恢复。
- 🚫 广告在源头处理，而不是播放后跳过。
- 🎧 基于相同录音校验的 FLAC / 高解析度下载。
- 🎤 更多歌词源、逐字歌词和 Genius 歌曲说明。
- 🎬 带有独立音轨的全屏音乐视频。
- 👥 协作列表、从列表内添加歌曲、更多列表编辑功能。
- 🔀 智能随机播放、可拖动队列、交叉淡入淡出。
- 🎙️ 播客和有声读物、下载及专属播放控件。
- 📷 Spotify Code 分享、个人资料、最近播放、分类浏览和新歌。
- 🌍 多语言与应用内更新、便捷诊断报告。

详细记录见 [CHANGELOG.md](CHANGELOG.md)。**请勿将上游的版本更新记录理解为本汉化仓库已发布了同版本 APK**。

## 软件截图

以下沿用**原项目截图**，用于展示界面布局；截图可能仍为英文，不能据此认定汉化版所有界面已经完成实机验收。

| 首页 | 播放器 | 歌手 | 专辑 |
|:---:|:---:|:---:|:---:|
| <img src="docs/screenshots/home.jpg" width="200" alt="首页"> | <img src="docs/screenshots/player.jpg" width="200" alt="播放器"> | <img src="docs/screenshots/artist.jpg" width="200" alt="歌手"> | <img src="docs/screenshots/album.jpg" width="200" alt="专辑"> |

## 汉化分支与当前完成范围

| 项目 | 状态 |
|---|---|
| 上游项目 | [kota-zo/myspoti](https://github.com/kota-zo/myspoti) |
| 汉化源代码 | [`i18n/zh-hans`](https://github.com/HypnosysNyx/myspoti/tree/i18n/zh-hans) |
| 汉化基线 | 上游 2026-10-23 的 `3ab91a0` 提交 |
| Android 字符串资源 | `myspoti_strings.xml` 493 项普通字符串 + 3 组复数；`strings.xml` 38 项非品牌翻译 |
| 汉化静态 QA | 已有资源键、格式占位符和部分渲染调用的检查 |
| Android APK / 实机验收 | **必须以对应提交实际构建和设备测试为准；静态检查不代表全部汉化完成** |
| 许可证 | [GPL-3.0](LICENSE) |

### 自行编译中文版

请**先切换到汉化分支**，不要从本仓库仍含英文原资源的其他分支直接构建并称为中文版。需要 JDK 17+ 和 Android SDK（`compileSdk 37`；CI 使用 JDK 21）。

```bash
git clone --branch i18n/zh-hans https://github.com/HypnosysNyx/myspoti.git
cd myspoti
python3 tools/check_zh_localization.py --project .
python3 -m unittest discover -s tests -p 'test_zh_localization.py'
cd base
./gradlew assembleDebug
./gradlew testDebugUnitTest
```

Windows 使用 `.\gradlew.bat assembleDebug`。编译后的测试 APK 通常在 `base/app/build/outputs/apk/debug/`。**Debug 包使用测试签名与开发版应用 ID（带 `.dev` 后缀），不等同于可自动升级的正式发布版。**

开发者文档：[Spotify API 模块](base/api-spotify/README.md)、[API 资料](docs/api)、[本地化 QA](https://github.com/HypnosysNyx/myspoti/blob/i18n/zh-hans/docs/localization-QA-report-zh-CN.md)。

### 开发结构

Android 项目位于 `base/`：

- `:api`：播放器、搜索、音乐目录、播放列表、歌词、设备和 Jam 等功能的数据结构与接口。
- `:api-spotify`：基于 Spotify Web Player 的 API 实现，由隐藏的 WebView 宿主及 Bridge 驱动；搜索与音乐库数据直接取自 Spotify。
- `:host-cdp`：通过桌面 Chrome 对真实 Web Player 执行 API 测试。

可选的在线 API 测试（需要已登录 Spotify Web Player 的桌面 Chrome）：

```bash
google-chrome --user-data-dir="$HOME/.myspoti-chrome" --remote-debugging-port=9222
./gradlew :host-cdp:test -Pcdp=http://localhost:9222
```

## 常见问题

**登录会泄露 Spotify 密码吗？** 登录过程使用 Spotify 页面，而不是把密码交给汉化作者；但仍应自行评估第三方客户端的账号风险。

**提示“Spotify 拒绝播放”？** 可能与地区、账号、设备、DRM 或 WebView 有关。更新 Android System WebView 与 Chrome；在应用内导出诊断报告，并向[本仓库 Issues](https://github.com/HypnosysNyx/myspoti/issues)反馈。提交前检查日志是否包含个人信息，不要上传令牌。

**离线下载会算入 Wrapped 吗？** 不会。正常在线流媒体播放与音乐视频可按 Spotify 自身机制计入播放历史；离线文件只计入本地回顾。

**有哪些数据会离开设备？** 播放请求会发送至 Spotify，歌词、Genius、Google 翻译、YouTube、Tidal/Qobuz 等对应服务可能接收其功能需要的请求；不要把“没有发送给原作者”理解为“不访问第三方服务”。

**中文界面还有英文怎么办？** 本分支主要翻译 Myspoti 自有的 Android 字符串资源，不覆盖 Spotify 官方网页、第三方服务响应、歌名与设备名称。可通过 [Issues](https://github.com/HypnosysNyx/myspoti/issues)提交截图、操作路径、系统语言及构建版本。

## 注意事项与免责声明

- 本项目**不绕过 Spotify 的 DRM，也不提供 Spotify 官方音频文件下载**。离线文件来自可用的第三方目录；没有匹配音源时可能无法下载。
- 广告拦截、修改版客户端及相关使用方式可能违反 Spotify 服务条款，并可能引起账号限制或封禁。使用者自行承担风险；在条件允许时请通过正规渠道支持音乐创作者。
- 本项目与 Spotify AB 无隶属、合作或授权关系；Spotify 为其权利人的商标。
- **中文汉化维护与原项目开发是两项不同工作。** 不要将本分支的问题报告误发给原作者，除非已确认问题存在于原版。

## 鸣谢、支持与许可证

**原项目及核心开发：** [kota-zo/myspoti](https://github.com/kota-zo/myspoti)，中文本地化由本仓库维护。原作者的 [Ko-fi](https://ko-fi.com/kotazo)、[GitHub Sponsors](https://github.com/sponsors/kota-zo) 和 [Discord 社区](https://discord.gg/jXKnGVFnGS)仍可用于支持上游与参与讨论（并非汉化维护者的赞助渠道）。

保留上游 README 所列的技术来源和授权：

- [Spotui](https://github.com/Spotui/Spotui) / [Metrolist](https://github.com/MetrolistGroup/Metrolist)（GPL-3.0）：界面基础，以及部分 Kotlin 无损解析、验证和音频封装代码。
- [SpotiFLAC](https://github.com/spotbye/SpotiFLAC)（MIT）：无损音源解析与社区后端协议。
- [SpotiFLAC Mobile](https://github.com/zarzet/SpotiFLAC-Mobile)（MIT）及其[扩展](https://github.com/zarzet/SpotiFLAC-Extension)（Apache-2.0）：下载会话及 Tidal / Qobuz 请求。
- [NewPipeExtractor](https://github.com/TeamNewPipe/NewPipeExtractor)（GPL-3.0）：音乐视频。
- 歌词来源： [LRCLIB](https://lrclib.net)、LyricsPlus、lrc.red、酷狗、网易云音乐；歌曲解读： [Genius](https://genius.com)。
- [Material Icons](https://github.com/google/material-design-icons)（Apache-2.0）、[Manrope 字体](https://github.com/googlefonts/manrope)（SIL OFL 1.1）。

完整第三方许可见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)、`base/licenses/`，项目遵循 [GNU GPL-3.0](LICENSE)。[阅读保存的英文原版说明](README.en.md)。
