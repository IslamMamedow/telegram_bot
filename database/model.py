from peewee import *
from loader import database


class DataBaseUser(Model):
    """
    Таблица в базе данных "user"
    telegram_id - ID  пользователя
    command - команда запроса
    request_time - время и дата запроса
    request_history - информация об отеле в формате JSON
    location - локация поиска
    """

    telegram_id = IntegerField(null=True)
    command = CharField(null=True)
    request_time = DateTimeField()
    request_history = TextField(null=True)
    location = CharField(null=True)

    class Meta:
        database = database
        db_table = 'users'


def create_db() -> None:
    """Функция создает базу данных если отсутствует"""

    try:
        database.connect()
        DataBaseUser.create_table()
    except InternalError as err:
        print(str(err))


def add_data_to_user(user_id, command, request_time, hotel_data, location) -> None:
    """Функция для добавления данных в базу данных"""

    with database:
        DataBaseUser.create(telegram_id=user_id,
                            command=command,
                            request_time=request_time,
                            request_history=hotel_data,
                            location=location
                            )
