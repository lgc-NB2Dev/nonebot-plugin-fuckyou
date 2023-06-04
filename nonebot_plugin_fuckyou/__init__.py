from nonebot.plugin import PluginMetadata

from .__main__ import get_phase
from .config import ConfigModel

__version__ = "0.1.4"
__plugin_meta__ = PluginMetadata(
    name="FuckYou",
    description=get_phase(),
    usage="与机器人对骂即可（关键词触发）",
    homepage="https://github.com/lgc-NB2Dev/nonebot-plugin-fuckyou",
    type="application",
    config=ConfigModel,
    supported_adapters=None,
    extra={"License": "MIT", "Author": "student_2333"},
)
