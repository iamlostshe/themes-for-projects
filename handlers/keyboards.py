'Клавиатуры (обработчики нажатий на кнопки)'

from os import getenv

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv

from utils.subject_db import get_subjects, random_theme

router = Router(name=__name__)


@router.callback_query()
async def callback_queryes(call: CallbackQuery) -> None:
    'Обработка нажатий на кнопки'
    if call.data == 'random_theme':
        sub, sec, the = random_theme()

        msg_text = (
            f'Предмет: <b>{sub}</b>\n'
            f'Подраздел: <b>{sec}</b>\n\n'
            f'Тема: <b>{the}</b>\n'
        )

        markup = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text='Случайная тема', callback_data='random_theme'),
                InlineKeyboardButton(text='Предметы', callback_data='subjects')
            ]
        ]

        )

        await call.message.edit_text(msg_text, reply_markup=markup)

    elif call.data == 'subjects':
        eng = {
            'Биология': 'bio',
            'География': 'geo',
            'Информатика': 'info',
            'Математика': 'matem',
            'Обществознание': 'society',
            'Химия': 'chemistry',
            'История': 'history',
            'Литература': 'literature',
            'Физика': 'phisis'
        }

        r = []
        for i in get_subjects():
            r.append(InlineKeyboardButton(text=i, callback_data=eng[i]))

        markup = InlineKeyboardMarkup(inline_keyboard=[r])

        await call.message.edit_text('Выбери предмет:', reply_markup=markup)
    else:
        eng = {
            'bio': 'Биология',
            'geo': 'География',
            'info': 'Информатика',
            'matem': 'Математика',
            'society': 'Обществознание',
            'chemistry': 'Химия',
            'history': 'История',
            'literature': 'Литература',
            'phisis': 'Физика'
        }

        sub, sec, the = random_theme(eng[call.data])

        msg_text = (
            f'Предмет: <b>{sub}</b>\n'
            f'Подраздел: <b>{sec}</b>\n\n'
            f'Тема: <b>{the}</b>\n'
        )

        markup = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text='Случайная тема', callback_data='random_theme'),
                InlineKeyboardButton(text='Предметы', callback_data='subjects')
            ],
            [
                InlineKeyboardButton(text=f'Случайная тема ({eng[call.data]})', callback_data=call.data)
            ]
        ]

        )

        await call.message.edit_text(msg_text, reply_markup=markup)
