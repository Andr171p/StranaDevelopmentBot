from aiogram.types import ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

from app.bot.keyboards.buttons import RolesButtons


async def roles_menu_kb() -> ReplyKeyboardMarkup:
    keyboard_list = [
        [KeyboardButton(text=RolesButtons.COPYWRITER)],
        [KeyboardButton(text=RolesButtons.SMM)],
        [KeyboardButton(text=RolesButtons.REDACTOR)],
        [KeyboardButton(text=RolesButtons.EMAIL)],
        [KeyboardButton(text=RolesButtons.CORRECTOR)]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Специалисты:"
    )
    return keyboard
