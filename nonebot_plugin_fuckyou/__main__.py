import random
from typing import List, Set

from nonebot import on_message
from nonebot.internal.adapter import Event
from nonebot.matcher import Matcher

from .config import config
from .const import DEFAULT_TRIGGER_WORDS, GENTLE, VIOLENT

try:
    from nonebot.adapters.onebot.v11 import MessageEvent as OBV11MsgEv
    from nonebot.adapters.onebot.v12 import MessageEvent as OBV12MsgEv
except:
    OBV11MsgEv = None
    OBV12MsgEv = None

try:
    from nonebot.adapters.telegram.event import MessageEvent as TGMsgEv
except:
    TGMsgEv = None


PHASES: List[str] = (GENTLE if config.fuckyou_gentle else []) + (
    VIOLENT if config.fuckyou_violent else []
)
TRIGGER_WORDS: Set[str] = DEFAULT_TRIGGER_WORDS | config.fuckyou_extend_words

if not PHASES:
    raise ValueError("请至少选择一个骂人词库")


def get_phase() -> str:
    return random.choice(PHASES)


# nb2 的 on_message 貌似不支持忽略大小写，自己写一个
def trigger_rule(event: Event):
    if config.fuckyou_tome and (not event.is_tome()):
        return False

    try:
        msg = event.get_plaintext().lower()
    except:
        return False

    return any(w in msg for w in TRIGGER_WORDS)


trigger_matcher = on_message(rule=trigger_rule, block=config.fuckyou_block)


@trigger_matcher.handle()
async def _(matcher: Matcher, event: Event):
    kwargs = {}

    if (OBV11MsgEv and isinstance(event, OBV11MsgEv)) or (
        OBV12MsgEv and isinstance(event, OBV12MsgEv)
    ):
        kwargs["reply_message"] = True

    elif TGMsgEv and isinstance(event, TGMsgEv):
        kwargs["reply_to_message_id"] = event.message_id

    await matcher.finish(get_phase(), **kwargs)
