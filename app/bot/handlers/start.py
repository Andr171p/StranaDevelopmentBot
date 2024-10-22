from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from app.bot.keyboards.main_menu import main_menu_kb
from app.bot.messages import Messages


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: Message) -> None:
    await message.answer(
        text=Messages.START_MESSAGE,
        reply_markup=await main_menu_kb()
    )

