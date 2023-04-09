import random

from nonebot.plugin import PluginMetadata

from . import __main__ as __main__
from .config import ConfigModel
from .const import GENTLE, VIOLENT

__version__ = "0.1.0"
__plugin_meta__ = PluginMetadata(
    "FuckYou",
    random.choice(GENTLE + VIOLENT),
    "与机器人对骂即可（关键词触发）",
    ConfigModel,
    {"License": "MIT", "Author": "student_2333"},
)
