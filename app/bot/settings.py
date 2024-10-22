from app.bot.keyboards.buttons import (
    MainMenuButtons,
    RolesButtons,
    BackButtons
)


MAIN_MENU_HANDLERS = MainMenuButtons.__dict__.values()
ROLES_HANDLERS = RolesButtons.__dict__.values()
BACK_HANDLERS = BackButtons.__dict__.values()

HANDLER_IGNORE = [
    "Инструкция", "Специалисты 🧑🏻‍💻", "Обратная связь 📨",
    "Копирайтер 📝", "Рерайтер 🖋️", "Редактор 📖", "Рассылка писем 📩", "Корректор 📑",
    "Назад ↩"
]
