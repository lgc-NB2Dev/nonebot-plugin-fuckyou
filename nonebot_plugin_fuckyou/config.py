from nonebot import get_driver
from pydantic import BaseModel


class ConfigModel(BaseModel):
    fuckyou_violent: bool = False


config: ConfigModel = ConfigModel.parse_obj(get_driver().config.dict())
