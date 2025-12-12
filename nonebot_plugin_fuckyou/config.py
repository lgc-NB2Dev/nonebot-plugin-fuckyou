import json
from pathlib import Path

from nonebot import get_plugin_config
from nonebot.compat import type_validate_json
from pydantic import BaseModel, FilePath


class ConfigModel(BaseModel):
    fuckyou_gentle: bool = True
    fuckyou_violent: bool = False
    fuckyou_use_builtin_gentle: bool = True
    fuckyou_use_builtin_violent: bool = True
    fuckyou_external_gentle_path: FilePath | None = None
    fuckyou_external_violent_path: FilePath | None = None

    fuckyou_use_builtin_words: bool = True
    fuckyou_extend_words: set[str] = set()
    fuckyou_tome: bool = True

    fuckyou_user_blacklist: set[str] = set()
    fuckyou_user_bl_to_wl: bool = False
    fuckyou_group_blacklist: set[str] = set()
    fuckyou_group_bl_to_wl: bool = False

    fuckyou_block: bool = False
    fuckyou_inspect: bool = False


config = get_plugin_config(ConfigModel)


def load_external_phase(p: Path):
    return type_validate_json(list[str], json.loads(p.read_text("u8")))
