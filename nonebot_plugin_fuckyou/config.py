from typing import Set

from nonebot import get_plugin_config
from pydantic import BaseModel


class ConfigModel(BaseModel):
    fuckyou_gentle: bool = True
    fuckyou_violent: bool = False
    fuckyou_tome: bool = True
    fuckyou_extend_words: Set[str] = set()
    fuckyou_block: bool = False

    fuckyou_blacklist: Set[str] = set()
    fuckyou_bl_to_wl: bool = False


config = get_plugin_config(ConfigModel)
