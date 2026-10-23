# QA 历史：Myspoti 简体中文

## 2026-10-23 — 首次简体中文资源覆盖

- **问题**：`values-zh` 仅包含原 Spotify 字符串资源，没有 Myspoti 自己的中文资源。因此切换 `zh` 后，Spotify 标签可以显示中文，而 Myspoti 设置、歌词、下载和提示文字仍会回退成英文。
- **原因**：默认 `values/myspoti_strings.xml`（493 条字符串、3 组复数）和 `values/strings.xml`（39 条，含不应翻译的应用品牌名称）缺少 `values-zh` 对应项；`AppLanguage.kt` 原本已经包含 `zh`，无须改动语言标签或持久化方式。
- **修复**：新增 `values-zh/myspoti_strings.xml` 与 `values-zh/strings.xml`，保留资源 ID、命名参数、顺序和品牌／协议标识；未改动 Kotlin 播放功能。
- **预防回归**：资源键全集的 FNV-1a 指纹、占位符清单、源资源对比脚本和 9 个精准翻译／渲染用例；优先覆盖 Welcome、Settings、Downloads、SpotiFLAC、MeaningSheet 与播放器设备面板。
- **静态验证**：XML 解析通过；新资源主文件 493 条文本和 3 组复数，通用文件 38 条文本；上游键名指纹吻合。来源固定在 `3ab91a07074abd7e23011245b8fa10afc0117b20`。
- **未验证**：完整仓库 Gradle 编译、Android 真机截图、TV 遥控器适配、第三方页面、应用运行时所有路径。需在相同源码提交的 APK 安装后逐屏复核。
