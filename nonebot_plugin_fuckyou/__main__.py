import random
from typing import List, Set
from typing_extensions import Annotated

from nonebot import logger, on_message
from nonebot.adapters import Event
from nonebot_plugin_alconna.uniseg import UniMessage
from nonebot_plugin_session import SessionId, SessionIdType

from .config import config, load_external_phase
from .const import DEFAULT_TRIGGER_WORDS, GENTLE, VIOLENT

PHASES: List[str] = [
    *(GENTLE if config.fuckyou_use_builtin_gentle and config.fuckyou_gentle else []),
    *(VIOLENT if config.fuckyou_use_builtin_violent and config.fuckyou_violent else []),
    *(
        load_external_phase(p)
        if (p := config.fuckyou_external_gentle_path) and config.fuckyou_gentle
        else []
    ),
    *(
        load_external_phase(p)
        if (p := config.fuckyou_external_violent_path) and config.fuckyou_violent
        else []
    ),
]
if not PHASES:
    raise ValueError("请至少选择一个骂人词库")

TRIGGER_WORDS: Set[str] = (
    DEFAULT_TRIGGER_WORDS if config.fuckyou_use_builtin_words else set()
) | config.fuckyou_extend_words


GroupID = Annotated[
    str,
    SessionId(
        SessionIdType.GROUP,
        include_bot_type=False,
        include_bot_id=False,
    ),
]


def get_phase() -> str:
    return random.choice(PHASES)


# nb2 的 on_message 貌似不支持忽略大小写，自己写一个
def trigger_rule(event: Event, group_id: GroupID):
    if config.fuckyou_tome and (not event.is_tome()):
        return False

    in_user_blacklist = event.get_user_id() in config.fuckyou_user_blacklist
    if config.fuckyou_user_bl_to_wl:
        in_user_blacklist = not in_user_blacklist
    in_group_blacklist = group_id in config.fuckyou_group_blacklist
    if config.fuckyou_group_bl_to_wl:
        in_group_blacklist = not in_group_blacklist
    if any((in_user_blacklist, in_group_blacklist)):
        return False

    try:
        msg = event.get_plaintext().lower()
    except Exception:
        return False

    return any(w in msg for w in TRIGGER_WORDS)


trigger_matcher = on_message(rule=trigger_rule, block=config.fuckyou_block)


@trigger_matcher.handle()
async def _(group_id: GroupID):
    if config.fuckyou_inspect:
        logger.success(group_id)
    phase = get_phase()
    await UniMessage(phase).send(reply_to=True)
