from aiogram.types import ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

from app.bot.keyboards.buttons import MainMenuButtons


async def main_menu_kb() -> ReplyKeyboardMarkup:
    keyboard_list = [
        [KeyboardButton(text=MainMenuButtons.INFO)],
        [KeyboardButton(text=MainMenuButtons.ROLES)],
        [KeyboardButton(text=MainMenuButtons.FEEDBACK)]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Главное меню"
    )
    return keyboard