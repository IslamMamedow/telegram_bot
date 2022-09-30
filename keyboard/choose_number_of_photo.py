from telebot.types import Message

from telebot import types
from loader import bot


def show_or_not_show_photo(message: Message) -> None:
    """Функция запрашивает надобность вывода фото отелей"""
    yes_no_buttons = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text='Да',
            callback_data='with_photo'
        ),
        types.InlineKeyboardButton(
            text='Нет',
            callback_data='without_photo'
        )
    )

    bot.send_message(chat_id=message.chat.id,
                     text='Показывать фото отелей?',
                     reply_markup=yes_no_buttons)


def choice_number(message: Message) -> None:
    """Функция выводит inline кнопки для выбора количества отелей"""

    number_buttons = types.InlineKeyboardMarkup().add(
        *[types.InlineKeyboardButton(
            text=str(numb),
            callback_data='ch' + str(numb))
            for numb in range(1, 11)])

    bot.send_message(chat_id=message.chat.id,
                     text='Выберете количество фотографий:',
                     reply_markup=number_buttons)
