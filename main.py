import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import TOKEN
from app.bot.handlers.start import start_router
from app.bot.handlers.main_menu import main_menu_router
from app.bot.handlers.roles import roles_router
from app.bot.handlers.dialog import dialog_router
from app.bot.handlers.back import back_router
from app.bot.handlers.feedback import feedback_router


bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
dp.include_routers(
    start_router,
    feedback_router,
    main_menu_router,
    roles_router,
    back_router,
    dialog_router
)


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
