from typing import List, Optional, Type

import aiogram

from app.internal.telegram.keyboards.base_keyboard import BaseKeyboard

__all__ = [
    "set_in_state_last_message",
    "get_from_state_last_message",
    "set_in_state_buttons",
    "get_from_state_buttons",
]


async def set_in_state_last_message(
    state: aiogram.dispatcher.FSMContext,
    message: aiogram.types.Message,
) -> None:
    await state.update_data(last_message=message)


async def get_from_state_last_message(
    state: aiogram.dispatcher.FSMContext,
) -> Optional[aiogram.types.Message]:
    async with state.proxy() as state_data:
        return state_data.get("last_message", None)


async def set_in_state_buttons(
    state: aiogram.dispatcher.FSMContext,
    buttons: List[Type[BaseKeyboard]],
) -> None:
    await state.update_data(buttons=buttons)


async def get_from_state_buttons(
    state: aiogram.dispatcher.FSMContext,
) -> Optional[Type[BaseKeyboard]]:
    async with state.proxy() as state_data:
        return state_data.get("buttons", None)
