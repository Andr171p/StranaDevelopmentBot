from aiogram import F, Router
from aiogram.types import Message

from app.bot.messages import MainMenuMessages
from app.bot.keyboards.buttons import MainMenuButtons
from app.bot.keyboards.main_menu import main_menu_kb
from app.bot.keyboards.roles_menu import roles_menu_kb


main_menu_router = Router()


@main_menu_router.message(F.text == MainMenuButtons.INFO)
async def info_handler(message: Message) -> None:
    await message.answer(
        text=MainMenuMessages.INFO_MESSAGE,
        reply_markup=await main_menu_kb()
    )


@main_menu_router.message(F.text == MainMenuButtons.ROLES)
async def roles_handler(message: Message) -> None:
    await message.answer(
        text=MainMenuMessages.ROLES_MESSAGE,
        reply_markup=await roles_menu_kb()
    )


@main_menu_router.message(F.text == MainMenuButtons.FEEDBACK)
async def feedback_handler(message: Message) -> None:
    ...
