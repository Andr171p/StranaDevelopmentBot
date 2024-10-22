from aiogram import F, Router
from aiogram.types import Message

from app.bot.messages import RolesMessage
from app.bot.keyboards.buttons import RolesButtons
from app.bot.keyboards.roles_menu import roles_menu_kb

from llm.model.giga_chat import GigaChatModel, giga_chat_model
from llm.prompt.template import GigaChatPrompts


roles_router = Router()

giga_chat_prompts = GigaChatPrompts


@roles_router.message(F.text == RolesButtons.COPYWRITER)
async def copywriter_handler(message: Message) -> None:
    copywriter_prompt = giga_chat_prompts(chat='copywriter').prompt()
    giga_chat_model.model()
    giga_chat_model.system_message(message=copywriter_prompt)
    await message.answer(
        text=RolesMessage.COPYWRITER_MESSAGE,
        reply_markup=await roles_menu_kb()

    )


@roles_router.message(F.text == RolesButtons.SMM)
async def smm_handler(message: Message) -> None:
    smm_prompt = giga_chat_prompts(chat='rewriter').prompt()
    giga_chat_model.model()
    giga_chat_model.system_message(message=smm_prompt)
    await message.answer(
        text=RolesMessage.SMM_MESSAGE,
        reply_markup=await roles_menu_kb()
    )


@roles_router.message(F.text == RolesButtons.REDACTOR)
async def redactor_handler(message: Message) -> None:
    redactor_prompt = giga_chat_prompts(chat='redactor').prompt()
    giga_chat_model.model()
    giga_chat_model.system_message(message=redactor_prompt)
    await message.answer(
        text=RolesMessage.REDACTOR_MESSAGE,
        reply_markup=await roles_menu_kb()
    )


@roles_router.message(F.text == RolesButtons.EMAIL)
async def email_handler(message: Message) -> None:
    email_prompt = giga_chat_prompts(chat='email').prompt()
    giga_chat_model.model()
    giga_chat_model.system_message(message=email_prompt)
    await message.answer(
        text=RolesMessage.EMAIL_MESSAGE,
        reply_markup=await roles_menu_kb()
    )


@roles_router.message(F.text == RolesButtons.CORRECTOR)
async def corrector_handler(message: Message) -> None:
    corrector_prompt = giga_chat_prompts(chat='corrector').prompt()
    giga_chat_model.model()
    giga_chat_model.system_message(message=corrector_prompt)
    await message.answer(
        text=RolesMessage.CORRECTOR_MESSAGE,
        reply_markup=await roles_menu_kb()
    )
