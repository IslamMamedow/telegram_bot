import json
import requests
from datetime import datetime

from states.user import User
import telebot
from loader import bot, rapid_key
from telebot import types
from database.model import add_data_to_user


def print_hotel_and_photo(message: telebot.types.Message, hotel) -> None:
    """Функция обрабатывает данные отелей и отправляет запрос на получение фото"""

    user = User.get_user(message.from_user.id)

    user.hotels_count += 1
    stars = int(hotel["starRating"])
    total_sum = int(float(hotel["ratePlan"]["price"]["exactCurrent"]) * user.nights_number)
    total_sum_str = '{:,}'.format(total_sum)

    star_string = '\U0001F4C8 Рейтинг(Звездность): ' + '\U00002B50' * stars if stars > 1 \
        else '\U0001F4C8 Рейтинг(Звездность): \U0000274C'
    current = ' $' if user.language_code == 'en_US' else ' RUB'

    text = f'\U0001F3E8  {hotel["name"]}\n\n' \
           f'\U0001F5FA Адрес: {hotel["address"].get("streetAddress")}\n' + \
           star_string + \
           f'\n\U0001F4CD Расстояние до центра: {hotel["landmarks"][0]["distance"]}\n' \
           f'\U0001F4B5 Цена за ночь: {hotel["ratePlan"]["price"]["current"]}\n' + \
           f'\U0001F9FE Общая сумма за {user.nights_number} ночь(ей): {total_sum_str}' + current

    next_and_site_button = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text='Сайт отеля',
                                   url=f'https://ie.hotels.com/ho{hotel["id"]}'),
        types.InlineKeyboardButton(text='\U00002935 Показать следующий отель \U00002935',
                                   callback_data='next_hotel'),
        row_width=True
    )

    if user.show_photo:
        url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"

        querystring = {"id": hotel["id"]}

        headers = {
            "X-RapidAPI-Key": rapid_key,
            "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        if response:
            data = json.loads(response.text)['hotelImages']
            photos = [data[i]['baseUrl'].format(size='z') for i in range(user.number_of_photo)]

            media_group = [types.InputMediaPhoto(media=url) for url in photos]
            try:
                bot.send_media_group(chat_id=message.chat.id,
                                     media=media_group)
            except BaseException as err:
                print(err)
                bot.send_media_group(chat_id=message.chat.id,
                                     media=media_group)

    bot.send_message(chat_id=message.chat.id,
                     text=text,
                     reply_markup=next_and_site_button)

    add_data_to_user(user_id=user.user_id,
                     command=user.command,
                     request_time=str(datetime.now()),
                     hotel_data={
                         'dates': [str(user.arrival_date), str(user.departure_date)],
                         'nights': user.nights_number,
                         'photos': photos if user.show_photo else None,
                         'hotel_data': text,
                         'hotel_site': f'https://ie.hotels.com/ho{hotel["id"]}'
                     },
                     location=user.location
                     )
