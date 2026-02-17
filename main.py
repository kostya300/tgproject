from typing import Any, List
from tkinter import *
from tkinter.ttk import *
from dataclasses import dataclass
from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    host: str  # URL-адрес базы данных
    user: str  # Username пользователя базы данных
    password: str  # Пароль к базе данных
    database: str  # Название базы данных


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    bot: TgBot
    db: DatabaseConfig

config = Config(
    bot=TgBot(token=BOT_TOKEN, admin_ids=ADMIN_IDS),
    db=DatabaseConfig(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DATABASE
    )

)