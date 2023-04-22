from nonebot.plugin import PluginMetadata

from .__main__ import get_phase
from .config import ConfigModel

__version__ = "0.1.2"
__plugin_meta__ = PluginMetadata(
    "FuckYou",
    get_phase(),
    "与机器人对骂即可（关键词触发）",
    ConfigModel,
    {"License": "MIT", "Author": "student_2333"},
)
