import random
from typing import List

from nonebot import on_message
from nonebot.internal.adapter import Event
from nonebot.matcher import Matcher

from .config import config
from .const import GENTLE, TRIGGER_WORDS, VIOLENT

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


phases: List[str] = VIOLENT if config.fuckyou_violent else GENTLE


# nb2 的 on_message 貌似不支持忽略大小写，自己写一个
def trigger_rule(event: Event):
    if not event.is_tome():
        return False

    try:
        msg = event.get_plaintext().lower()
    except:
        return False

    return any(w in msg for w in TRIGGER_WORDS)


trigger_matcher = on_message(rule=trigger_rule)


@trigger_matcher.handle()
async def _(matcher: Matcher, event: Event):
    kwargs = {}

    if (OBV11MsgEv and isinstance(event, OBV11MsgEv)) or (
        OBV12MsgEv and isinstance(event, OBV12MsgEv)
    ):
        kwargs["reply_message"] = True

    elif TGMsgEv and isinstance(event, TGMsgEv):
        kwargs["reply_to_message_id"] = event.message_id

    await matcher.finish(random.choice(phases), **kwargs)
