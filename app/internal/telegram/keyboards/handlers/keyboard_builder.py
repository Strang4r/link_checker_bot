from typing import List, Type

import aiogram.types

from app.internal.telegram.keyboards.base_keyboard import BaseKeyboard


async def build_markup(
    buttons: List[Type[BaseKeyboard]],
) -> aiogram.types.InlineKeyboardMarkup:
    """Build markup for message.

    Args:
        buttons:  by list of buttons inherited by ``BaseKeyboard``.

    Examples:

        bot.send_message(
            ...,
            reply_markup=build_markup(buttons=[ETHFullNode, BTCNode, ETHLightNode])
        )

    Returns:
        aiogram.types.InlineKeyboardMarkup.
    """
    mp = aiogram.types.InlineKeyboardMarkup()
    for button in buttons:
        b = button()
        mp.add(await b.get_button())
    return mp
