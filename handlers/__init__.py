'Собирает все роутеры во-едино'

# Импортируем все обработчики
from handlers import (
    start,
    keyboards
)

routers = (
    start.router,
    keyboards.router
)

__all__ = ("routers",)
