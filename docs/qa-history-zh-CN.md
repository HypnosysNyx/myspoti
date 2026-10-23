# QA 历史：Myspoti 简体中文

## 2026-10-23 — 首次简体中文资源覆盖

- **问题**：`values-zh` 仅包含原 Spotify 字符串资源，没有 Myspoti 自己的中文资源。因此切换 `zh` 后，Spotify 标签可以显示中文，而 Myspoti 设置、歌词、下载和提示文字仍会回退成英文。
- **原因**：默认 `values/myspoti_strings.xml`（493 条字符串、3 组复数）和 `values/strings.xml`（39 条，含不应翻译的应用品牌名称）缺少 `values-zh` 对应项；`AppLanguage.kt` 原本已经包含 `zh`，无须改动语言标签或持久化方式。
- **修复**：新增 `values-zh/myspoti_strings.xml` 与 `values-zh/strings.xml`，保留资源 ID、命名参数、顺序和品牌／协议标识；未改动 Kotlin 播放功能。
- **预防回归**：资源键全集的 FNV-1a 指纹、占位符清单、源资源对比脚本和 9 个精准翻译／渲染用例；优先覆盖 Welcome、Settings、Downloads、SpotiFLAC、MeaningSheet 与播放器设备面板。
- **静态验证**：XML 解析通过；新资源主文件 493 条文本和 3 组复数，通用文件 38 条文本；上游键名指纹吻合。来源固定在 `3ab91a07074abd7e23011245b8fa10afc0117b20`。
- **未验证**：完整仓库 Gradle 编译、Android 真机截图、TV 遥控器适配、第三方页面、应用运行时所有路径。需在相同源码提交的 APK 安装后逐屏复核。

## 2026-10-23 — 交叉淡入淡出 12 秒按钮排版回归

- **问题**：简体中文设置页在较大系统字体/较窄屏幕下，第五个 `12 秒` 选项挤成竖排的 `1 / 2 / 秒`。
- **原因**：`CrossfadeRow()` 用不可换行的单行 `Row` 排列 5 个带内边距的 `Text` 按钮，前 4 个占满空间后最后一个只收到极窄宽度，Compose 逐字符断行。
- **修复**：仅将该设置项换成 `FlowRow`，在空间不足时整颗按钮换到下一行；加 `maxLines = 1` 和 `softWrap = false` 防止文字拆行。保持 `0,3,6,9,12`、资源键、点击保存及实际淡入淡出行为不变。
- **回归**：新增截图案例 `settings-crossfade-chip-wrap-zh`，并对恢复 `Row`、删除单行保护两种根因做反向失败测试。
- **验证限制**：源码/CI 通过不能代替安装相同提交 APK 后在大字体的安卓手机上检查排版。
