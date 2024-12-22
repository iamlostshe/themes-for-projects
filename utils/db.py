'Модуль для работы с JSON базой данных'

import json
import time
from os.path import exists

from loguru import logger


async def add_user(
    user_id: int | str,
    sourse: str,
    first_name: str,
    last_name: str,
    is_premium: bool,
    language_code: str,
    username: str
):
    'Добавляет пользователя в JSON базу данных'
    user_id = str(user_id)

    with open('index.json', 'r+', encoding='UTF-8') as f:
        data = json.load(f)

        if not data.get(user_id):
            new_user = {
                'time': time.time(),
                'sourse': sourse,
                'first_name': first_name,
                'last_name': last_name,
                'is_premium': is_premium,
                'language_code': language_code,
                'username': username
            }

            data[user_id] = new_user

        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4, ensure_ascii=False)

    logger.debug('Новый пользователь! {}', user_id)


async def check_db():
    'Проверяет наличае файла бд в папке и создает его при необходимости'
    if not exists('index.json'):
        with open('index.json', 'a', encoding='UTF-8') as f:
            f.write('{}')
