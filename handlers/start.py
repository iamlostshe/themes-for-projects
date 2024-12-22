'Приветственное сообщение'

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils import db


router = Router(name=__name__)


@router.message(CommandStart())
async def all_messages(msg: Message) -> None:
    'Обработка входящих сообщений'
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Случайная тема', callback_data='random_theme'),
            InlineKeyboardButton(text='Предметы', callback_data='subjects')
        ]
    ])

    await msg.answer(
        (
            f'👋 Привет, {msg.from_user.first_name}".\n\n'
            '🤖 Этот бот поможет тебе выбрать тему для школьного проекта/диплома.\n\n'
            '📌 Нажми на кнопку ниже, чтобы продолжить.'
        ),
        reply_markup=markup
    )

    await db.add_user(
        msg.from_user.id,
        msg.text[7:],
        msg.from_user.first_name,
        msg.from_user.last_name,
        msg.from_user.is_premium,
        msg.from_user.language_code,
        msg.from_user.username
    )