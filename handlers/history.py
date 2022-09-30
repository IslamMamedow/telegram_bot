from telebot.types import Message
from telebot import types
from states.user import User
from loader import database, bot
from database.model import DataBaseUser


def print_history(message: Message) -> None:
    """Функция делает SELECT запрос к базе данных, обрабатывает и отправляет запрос пользователю"""

    user = User.get_user(message.from_user.id)

    with database:
        request = DataBaseUser.select().where(DataBaseUser.telegram_id == user.user_id)

        if len(request) != 0:
            bot.send_message(chat_id=message.chat.id,
                             text='Ваша история поиска:'
                             )
            for data in request:
                hotel = eval(data.request_history.replace('????', ''))

                text = f'{data.command}\n' \
                       f'Локация поиска: {data.location}\n' \
                       f'Время обращения: {data.request_time}\n\n' \
                       f'Дата пребывания:\n' \
                       f'     \U00002B07Заезд: {hotel["dates"][0]}\n' \
                       f'     \U00002B06Выезд: {hotel["dates"][1]}\n' \
                       f'     \U0001F303{hotel["nights"]} ночей\n\n' \
                       f'\U0001F3E8Отель:{hotel["hotel_data"]}'
                if hotel['photos'] is not None:
                    bot.send_media_group(chat_id=message.chat.id,
                                         media=[types.InputMediaPhoto(media=url) for url in hotel['photos']])

                bot.send_message(chat_id=message.chat.id,
                                 text=text,
                                 reply_markup=types.InlineKeyboardMarkup().add(
                                     types.InlineKeyboardButton(text='Сайт отеля',
                                                                url=hotel['hotel_site']
                                                                )
                                 ))
        else:
            bot.send_message(chat_id=message.chat.id,
                             text='История поиска пуста.')
