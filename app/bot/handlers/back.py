from aiogram import F, Router
from aiogram.types import Message

from app.bot.messages import MainMenuMessages
from app.bot.keyboards.buttons import BackButtons
from app.bot.keyboards.main_menu import main_menu_kb


back_router = Router()


@back_router.message(F.text == BackButtons.BACK)
async def back_handler(message: Message) -> None:
    await message.answer(
        text=MainMenuMessages.COMEBACK_TO_MAIN_MENU,
        reply_markup=await main_menu_kb()
    )
