from nonebot.plugin import PluginMetadata, inherit_supported_adapters, require

require("nonebot_plugin_alconna")
require("nonebot_plugin_session")

from .__main__ import get_phase  # noqa: E402
from .config import ConfigModel  # noqa: E402

__version__ = "0.3.0"
__plugin_meta__ = PluginMetadata(
    name="FuckYou",
    description=get_phase(),
    usage="与机器人对骂即可（关键词触发）",
    homepage="https://github.com/lgc-NB2Dev/nonebot-plugin-fuckyou",
    type="application",
    config=ConfigModel,
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_alconna",
        "nonebot_plugin_session",
    ),
    extra={"License": "MIT", "Author": "student_2333"},
)
