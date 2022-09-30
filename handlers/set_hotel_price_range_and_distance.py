from telebot.types import Message
from telebot import types

from loader import bot
from states.user import User
from keyboard import choose_number_of_photo


def set_price_range(message: Message) -> None:
    """Функция запрашивает диапазон цен для запроса /bestdeal"""

    user = User.get_user(message.from_user.id)
    message_from_user = bot.send_message(chat_id=message.chat.id,
                                         text='Введите диапазон цен:\n'
                                              'Пример ввода: 150-830')
    bot.register_next_step_handler(message=message_from_user,
                                   callback=is_correct_range)


def is_correct_range(message: Message) -> None:
    """Функция проверяет корректность ввода диапазона цен"""

    user = User.get_user(message.from_user.id)
    price_range = message.text.split('-')

    if len(price_range) == 2:

        if price_range[0].isdigit() and price_range[1].isdigit():
            first_numb, second_numb = int(price_range[0]), int(price_range[1])

            if first_numb < second_numb:
                user.price_min, user.price_max = first_numb, second_numb
            else:
                user.price_max, user.price_min = first_numb, second_numb

            yes_no_button = types.InlineKeyboardMarkup(). \
                add(types.InlineKeyboardButton(text='Да',
                                               callback_data='center_correct_data'),
                    types.InlineKeyboardButton(text='Нет',
                                               callback_data='center_incorrect_data'))
            current = '$' if user.language_code == 'en_US' else 'RUB'
            return bot.send_message(chat_id=message.chat.id,
                                    text=f'Минимальная цена: {user.price_min} {current}\n'
                                         f'Максимальная цена: {user.price_max} {current}\n'
                                         'Данные указаны верно?',
                                    reply_markup=yes_no_button)

    message_from_user = bot.send_message(chat_id=message.chat.id,
                                         text='\U00002757 Ошибка: Неправильный ввод диапазона\n'
                                              'Пример ввода(100-3000)'
                                              'Попробуйте снова:\n')
    bot.register_next_step_handler(message=message_from_user,
                                   callback=is_correct_range)


def get_max_distance_from_center(message: Message) -> None:
    """Функция запрашивает максимальное расстояние от центра города"""

    message_from_user = bot.send_message(chat_id=message.chat.id,
                                         text='Введите максимальное расстояние от центра города(в км):')
    bot.register_next_step_handler(message=message_from_user,
                                   callback=set_max_distance_from_center)


def set_max_distance_from_center(message: Message) -> None:
    user = User.get_user(message.from_user.id)

    if message.text.isdigit():
        if int(message.text) > 0:
            user.max_distance = message.text
            return choose_number_of_photo.show_or_not_show_photo(message)

    message_from_user = bot.send_message(chat_id=message.chat.id,
                                         text='Число должно быть положительным\n'
                                              'Введите максимальное расстояние еще раз: ')
    bot.register_next_step_handler(message=message_from_user,
                                   callback=set_max_distance_from_center)
