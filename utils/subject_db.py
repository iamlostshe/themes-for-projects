'Модуль для работы с JSON базой данных тем для проектов'

import json
import random


def random_theme(subject: str | None = None) -> tuple:
    'Возвращает случайную тему для проекта из базы'

    with open('subjects.json', 'r+', encoding='UTF-8') as f:
        data = json.load(f)

    # Задаём предмет если он не задан
    if not subject:
        r = []
        for i in data:
            r.append(i)
        subject = random.choice(r)

    # Задаём подтему (секцию)
    r = []
    for i in data[subject]:
        r.append(i)

    section = random.choice(r)

    # Задаём тему
    r = []
    for i in data[subject][section]:
        r.append(i)

    theme = random.choice(r)

    return subject, section, theme


def get_subjects():
    'Возвращает всевозможные для выбора предметы из базы'

    with open('subjects.json', 'r+', encoding='UTF-8') as f:
        data = json.load(f)

    r = []
    for i in data:
        r.append(i)
    
    return r
