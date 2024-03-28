<!-- markdownlint-disable MD031 MD033 MD036 MD041 -->

<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/fuckyou/logo.png" width="180" height="180" alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText">
</p>

# NoneBot-Plugin-FuckYou

_😅 你有几个 🐴，这么狂？ 😅_

<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">
<a href="https://pdm.fming.dev">
  <img src="https://img.shields.io/badge/pdm-managed-blueviolet" alt="pdm-managed">
</a>
<a href="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/fc345158-9120-4888-9a92-da01d63dc670">
  <img src="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/fc345158-9120-4888-9a92-da01d63dc670.svg" alt="wakatime">
</a>

<br />

<a href="https://pydantic.dev">
  <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/pyd-v1-or-v2.json" alt="Pydantic Version 1 Or 2" >
</a>
<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/lgc-NB2Dev/nonebot-plugin-fuckyou.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-fuckyou">
  <img src="https://img.shields.io/pypi/v/nonebot-plugin-fuckyou.svg" alt="pypi">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-fuckyou">
  <img src="https://img.shields.io/pypi/dm/nonebot-plugin-fuckyou" alt="pypi download">
</a>

</div>

## 📖 介绍

_10 分钟紧急开发的插件（误_

NoneBot2 骂人插件，攻击性极强

插件词库来源：[xiaoye12123/js](https://gitee.com/xiaoye12123/js)

有更多自定义配置项的 Fork (仅支持 OB V11): [Dogend233/nonebot-plugin-fuckyou-reset](https://github.com/Dogend233/nonebot-plugin-fuckyou-reset)

## 💿 安装

以下提到的方法 任选**其一** 即可

<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```bash
nb plugin install nonebot-plugin-fuckyou
```

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

```bash
pip install nonebot-plugin-fuckyou
```

</details>
<details>
<summary>pdm</summary>

```bash
pdm add nonebot-plugin-fuckyou
```

</details>
<details>
<summary>poetry</summary>

```bash
poetry add nonebot-plugin-fuckyou
```

</details>
<details>
<summary>conda</summary>

```bash
conda install nonebot-plugin-fuckyou
```

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分的 `plugins` 项里追加写入

```toml
[tool.nonebot]
plugins = [
    # ...
    "nonebot_plugin_fuckyou"
]
```

</details>

## ⚙️ 配置

在 nonebot2 项目的 `.env` 文件中添加下表中的必填配置

|             配置项              | 必填 | 默认值  |                                                  说明                                                   |
| :-----------------------------: | :--: | :-----: | :-----------------------------------------------------------------------------------------------------: |
|          **词库设置**           |      |         |                                                                                                         |
|        `FUCKYOU_GENTLE`         |  否  | `True`  |                                            是否启用温柔词库                                             |
|        `FUCKYOU_VIOLENT`        |  否  | `False` |                                            是否启用暴力词库                                             |
|  `FUCKYOU_USE_BUILTIN_GENTLE`   |  否  | `True`  |                              在启用温柔词库时，是否启用插件内置的温柔词库                               |
|  `FUCKYOU_USE_BUILTIN_VIOLENT`  |  否  | `True`  |           在启用暴力词库时，是否启用插件内置的暴力词库<br />**慎用，攻击性极强，后果自负**！            |
| `FUCKYOU_EXTERNAL_GENTLE_PATH`  |  否  | `None`  |                       要额外添加的温柔词库，请填写包含字符串数组的 JSON 文件路径                        |
| `FUCKYOU_EXTERNAL_VIOLENT_PATH` |  否  | `None`  |                       要额外添加的暴力词库，请填写包含字符串数组的 JSON 文件路径                        |
|          **触发设置**           |      |         |                                                                                                         |
|   `FUCKYOU_USE_BUILTIN_WORDS`   |  否  | `True`  |                                         是否使用插件内置触发词                                          |
|     `FUCKYOU_EXTEND_WORDS`      |  否  |  `[]`   |                                           要额外添加的触发词                                            |
|         `FUCKYOU_TOME`          |  否  | `True`  |                                      是否只有 @机器人 时才会骂回去                                      |
|          **黑白名单**           |      |         |                                                                                                         |
|    `FUCKYOU_USER_BLACKLIST`     |  否  |  `[]`   |                                         插件忽略的用户 ID 列表                                          |
|     `FUCKYOU_USER_BL_TO_WL`     |  否  | `False` |                                   是否将用户黑名单翻转变为白名单判断                                    |
|    `FUCKYOU_GROUP_BLACKLIST`    |  否  |  `[]`   | 插件忽略的群组 ID 列表<br />(为适配多平台，这里的 ID 不单单是群号，请参阅 `FUCKYOU_INSPECT` 配置项获取) |
|    `FUCKYOU_GROUP_BL_TO_WL`     |  否  | `False` |                                   是否将群组黑名单翻转变为白名单判断                                    |
|          **行为配置**           |      |         |                                                                                                         |
|         `FUCKYOU_BLOCK`         |  否  | `False` |                                            是否阻断 Matcher                                             |
|        `FUCKYOU_INSPECT`        |  否  | `False` |                          是否在触发插件功能后在 NoneBot 日志内打印当前群组 ID                           |

## 🎉 使用

直接 @Bot 对骂即可，插件为关键词检测，触发关键词可以看看 [const.py](./nonebot_plugin_fuckyou/const.py)

## 📞 联系

QQ：3076823485  
Telegram：[@lgc2333](https://t.me/lgc2333)  
吹水群：[1105946125](https://jq.qq.com/?_wv=1027&k=Z3n1MpEp)  
邮箱：<lgc2333@126.com>

## 💡 鸣谢

### [`xiaoye12123/js`](https://gitee.com/xiaoye12123/js)

- 攻击性极强的回复词库来源

## 💰 赞助

感谢大家的赞助！你们的赞助将是我继续创作的动力！

- [爱发电](https://afdian.net/@lgc2333)
- <details>
    <summary>赞助二维码（点击展开）</summary>

  ![讨饭](https://raw.githubusercontent.com/lgc2333/ShigureBotMenu/master/src/imgs/sponsor.png)

  </details>

## 📝 更新日志

### 0.3.0

- 引入 `alconna` 与 `session` 来实现平台特定操作
- 配置项更改：
  - 重命名 `FUCKYOU_BLACKLIST` -> `FUCKYOU_USER_BLACKLIST`
  - 重命名 `FUCKYOU_BL_TO_WL` -> `FUCKYOU_USER_BL_TO_WL`
  - 添加 `FUCKYOU_USE_BUILTIN_GENTLE`
  - 添加 `FUCKYOU_USE_BUILTIN_VIOLENT`
  - 添加 `FUCKYOU_EXTERNAL_GENTLE_PATH`
  - 添加 `FUCKYOU_EXTERNAL_VIOLENT_PATH`
  - 添加 `FUCKYOU_USE_BUILTIN_WORDS`
  - 添加 `FUCKYOU_GROUP_BLACKLIST`
  - 添加 `FUCKYOU_GROUP_BL_TO_WL`
  - 添加 `FUCKYOU_INSPECT`

### 0.2.0

- 适配 Pydantic V1 & V2

### 0.1.3

- 添加两个配置项

### 0.1.2

- 添加一个配置项

### 0.1.1

- 添加几个配置项
