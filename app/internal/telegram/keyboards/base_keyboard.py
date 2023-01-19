"""All keyboard objects must bt inherited by ``BaseKeyboard``.

Examples:
    If you need to get callback data, you just need to get attribute ``callback_data``
    from specific button.

        ListOfNodes.callback_data

If you need to build menu of buttons, you cat use ``build_markup``.
"""

import aiogram


class BaseKeyboard:
    callback_data: str
    text: str

    async def get_button(self) -> aiogram.types.InlineKeyboardButton:
        """Create ``aiogram.types.InlineKeyboardButton`` object by class
        attributes."""

        return aiogram.types.InlineKeyboardButton(
            text=self.text,
            callback_data=self.callback_data,
        )
