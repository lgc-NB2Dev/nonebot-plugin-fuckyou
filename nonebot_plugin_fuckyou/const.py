import json
from pathlib import Path

RESOURCE_DIR = Path(__file__).parent / "resource"
BUILTIN_GENTLE_PATH = RESOURCE_DIR / "builtin_gentle.json"
BUILTIN_VIOLENT_PATH = RESOURCE_DIR / "builtin_violent.json"

GENTLE: list[str] = json.loads(BUILTIN_GENTLE_PATH.read_text(encoding="u8"))
VIOLENT: list[str] = json.loads(BUILTIN_VIOLENT_PATH.read_text(encoding="u8"))

DEFAULT_TRIGGER_WORDS: set[str] = {
    "傻逼",
    "你妈逼",
    "日你妈",
    "草你妈",
    "操你妈",
    "cnm",
    "煞笔",
    "啥比",
    "杀币",
    "鲨臂",
    "shabi",
    "sb",
    "我是你爹",
}
