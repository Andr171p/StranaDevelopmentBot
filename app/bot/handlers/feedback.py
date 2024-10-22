from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.bot.messages import FeedbackMessage
from app.bot.keyboards.buttons import MainMenuButtons
from app.bot.keyboards.main_menu import main_menu_kb
from app.bot.states import UserCommentForm

from database.orm import orm_manager


feedback_router = Router()


@feedback_router.message(F.text == MainMenuButtons.FEEDBACK)
async def feedback_handler(message: Message,  state: FSMContext) -> None:
    await message.answer(
        text=FeedbackMessage.FEEDBACK_MESSAGE
    )
    await message.answer(
        text=FeedbackMessage.INPUT_COMMENT_MESSAGE,
        reply_markup=await main_menu_kb()
    )
    await state.set_state(UserCommentForm.comment)


@feedback_router.message(UserCommentForm.comment)
async def comment_handler(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    comment = message.text
    _ = await orm_manager.create_comment(
        user_id=user_id,
        username=username,
        comment=comment
    )
    await state.clear()
    await message.answer(
        text=FeedbackMessage.SUCCESSFULLY_SAVE_COMMENT_MESSAGE,
        reply_markup=await main_menu_kb()
    )
