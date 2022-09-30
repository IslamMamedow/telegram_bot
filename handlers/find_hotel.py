import json
import requests
import re

from states.user import User
import telebot
from loader import bot, rapid_key
from telebot import types

from handlers import set_hotel_price_range_and_distance
from handlers import print_hotel
from handlers import inline_handler


def remove_markup(location: str) -> str:
    """Функция для удаления HTML разметки """

    if '<' in location:
        pattern = re.compile('<.*?>')
        return pattern.sub('', location)
    return location


def language_detection(user_id, city) -> str:
    """Функция для определения кода языка и валюты"""

    user = User.get_user(user_id)

    if city[0].lower() in 'abcdefghijklmnopqrstuvwxyz':
        user.language_code = 'en_US'
        user.currency = 'USD'
        return 'en_US'
    user.language_code = 'ru_RU'
    user.currency = 'RUB'
    return 'ru_RU'


def search_city(message: telebot.types.Message) -> None:
    """Функция для определения города"""

    user = User.get_user(message.from_user.id)

    markup = types.InlineKeyboardMarkup()

    url = "https://hotels4.p.rapidapi.com/locations/v2/search"

    querystring = {"query": message.text,
                   "locale": language_detection(user_id=user.user_id, city=message.text),
                   "currency": user.currency}

    headers = {
        "X-RapidAPI-Key": rapid_key,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    loading_message = bot.send_message(message.chat.id, f'Идет поиск по по запросу "{message.text}"...')
    sticker_message = bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFxcpjF44JTURFZVJfab'
                                                        'exgXWSBX44uwACvxMAAtOBoUtbtqEavV924ykE')

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response:
        data = json.loads(response.text)
        if data:
            try:
                for location in data['suggestions'][0]['entities']:
                    location_without_markup = remove_markup(location['caption'])
                    location_id = location['destinationId']

                    location_button = types.InlineKeyboardButton(text='\U000027A1' + location_without_markup,
                                                                 callback_data=location_id)
                    user.location_id_with_locations_name[location_id] = location_without_markup

                    markup.add(location_button)

                try_button = types.InlineKeyboardButton(text='\U0001F501Ввести город повторно',
                                                        callback_data='try_again')
                markup.add(try_button)

                user.message_to_delete = bot.send_message(message.chat.id, f'Выберите локацию:', reply_markup=markup)
            except TypeError:
                message_from_user = bot.send_message(chat_id=message.chat.id,
                                                     text='\U0000203CОшибка поиска, '
                                                          'повторите запрос еще раз\U0000203C\n'
                                                          '\U0001F30F	Укажите город:')
                bot.register_next_step_handler(message=message_from_user,
                                               callback=search_city)
        else:
            message_from_user = bot.send_message(message.chat.id,
                                                 '\U0000274CОшибка поиска\U0000274C\n'
                                                 'Введите город снова: ')
            bot.register_next_step_handler(message_from_user, search_city)

    else:
        message_from_user = bot.send_message(message.chat.id, '\U0000274CГород не найден попробуйте снова\U0000274C')
        bot.register_next_step_handler(message_from_user, search_city)

    bot.delete_message(message.chat.id, loading_message.message_id)
    bot.delete_message(message.chat.id, sticker_message.id)


def get_hotel_list(message: telebot.types.Message) -> None:
    """Функция отправляет и принимает запрос на получение списка отелей по выбранной категории"""

    user = User.get_user(message.from_user.id)

    if user.hotels_count > 15:
        user.page_size += 1

    user.message_to_delete_id = bot.send_message(chat_id=message.chat.id,
                                                 text='Пожалуйста ожидайте. Идет поиск').message_id
    user.sticker_to_delete_id = bot.send_sticker(chat_id=message.chat.id,
                                                 sticker='CAACAgIAAxkBAAEFxcpjF44JTURFZVJfab'
                                                         'exgXWSBX44uwACvxMAAtOBoUtbtqEavV924ykE').message_id

    url = 'https://hotels4.p.rapidapi.com/properties/list'

    if user.command == '/lowprice' or user.command == '/highprice':

        querystring = {"destinationId": user.location_id,
                       "pageNumber": user.page_number,
                       "pageSize": user.page_size,
                       "checkIn": user.arrival_date,
                       "checkOut": user.departure_date,
                       "adults1": "2",

                       "sortOrder": 'PRICE' if user.command == '/lowprice' else
                       'PRICE_HIGHEST_FIRST',

                       "locale": 'en_US',
                       "currency": user.currency}

    elif user.command == '/bestdeal':
        querystring = {"destinationId": user.location_id,
                       "pageNumber": user.page_number,
                       "pageSize": user.page_size,
                       "checkIn": user.arrival_date,
                       "checkOut": user.departure_date,
                       "priceMin": user.price_min,
                       "priceMax": user.price_max,
                       "adults1": "2",
                       "sortOrder": 'DISTANCE_FROM_LANDMARK',
                       "locale": 'en_US',
                       "currency": user.currency}

    headers = {
        "X-RapidAPI-Key": rapid_key,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if response:
        data = json.loads(response.text)['data']['body']['searchResults']['results']

        if len(data) >= 1:
            if user.command == '/bestdeal':
                sorted_list_by_distance = [hotel for hotel in data
                                           if float(hotel['landmarks'][0]['distance'][:3]) <= int(user.max_distance)]
                if len(sorted_list_by_distance) > 1:
                    user.hotels_list = sorted_list_by_distance[:]
                else:

                    bot.send_message(chat_id=message.chat.id,
                                     text='\U0000274CПо вашему запросу отели не найдены\n'
                                          'Увеличьте максимальное расстояние поиска от центра города')
                    set_hotel_price_range_and_distance.get_max_distance_from_center(message)
            else:
                user.hotels_list = data[:]

            print_hotel.print_hotel_and_photo(message, user.hotels_list[user.hotels_count])

        else:
            bot.send_message(chat_id=message.chat.id,
                             text='\U0000274CПо вашему запросу отели не найдены\n'
                                  'Измените параметры запроса')
            message_from_user = bot.send_message(chat_id=message.chat.id,
                                                 text='\U0001F30F	Укажите город:')
            bot.register_next_step_handler(message=message_from_user,
                                           callback=search_city)

    else:
        message_from_user = bot.send_message(chat_id=message.chat.id,
                                             text='\U0000274CПроизошла ошибка попробуйте еще раз!\n'
                                                  'Введите город: ')
        bot.register_next_step_handler(message=message_from_user,
                                       callback=search_city)
    bot.delete_message(chat_id=message.chat.id,
                       message_id=user.message_to_delete_id)
    bot.delete_message(chat_id=message.chat.id,
                       message_id=user.sticker_to_delete_id)
