from typing import Set

from nonebot import get_driver
from pydantic import BaseModel


class ConfigModel(BaseModel):
    fuckyou_gentle: bool = True
    fuckyou_violent: bool = False
    fuckyou_tome: bool = True
    fuckyou_extend_words: Set[str] = set()
    fuckyou_block: bool = False


config: ConfigModel = ConfigModel.parse_obj(get_driver().config.dict())
