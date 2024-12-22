'Модуль запуска бота'

import asyncio
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from loguru import logger
from dotenv import load_dotenv

from handlers import routers
from utils import db

async def main() -> None:
    'Функция для запуска бота'
    # Подключаем файл для сбора логов
    logger.add('log.log')

    # Загружвем токен из .env
    load_dotenv()
    TOKEN = getenv("TOKEN")

    # Инициализируем диспетчер и бота
    dp = Dispatcher()
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Подключаем роутеры
    for r in routers:
        logger.info('Include router: {} ...', r.name)
        dp.include_router(r)

    # Проверяем наличае бд
    await db.check_db()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())