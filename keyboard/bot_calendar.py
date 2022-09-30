from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from loader import bot
from datetime import date, timedelta
from states.user import User
from telebot import types


def set_arrival_date(message):
    user = User.get_user(message.from_user.id)

    user.message_to_delete = bot.send_message(message.chat.id, "Введите дату заезда:")

    calendar, step = DetailedTelegramCalendar(calendar_id=1,
                                              current_date=date.today(),
                                              min_date=date.today(),
                                              max_date=date.today() + timedelta(days=365),
                                              locale="ru").build()
    bot.send_message(message.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=1))
def handle_arrival_date(call):
    user = User.get_user(call.from_user.id)

    result, key, step = DetailedTelegramCalendar(calendar_id=1,
                                                 current_date=date.today(),
                                                 min_date=date.today(),
                                                 max_date=date.today() + timedelta(days=365),
                                                 locale="ru").process(call.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        user.arrival_date = result

        bot.edit_message_text(f"\U00002B07 Дата заезда {user.arrival_date}",
                              call.message.chat.id,
                              call.message.message_id)

        bot.delete_message(call.message.chat.id, user.message_to_delete.message_id)

        user.message_to_delete = bot.send_message(user.user_id, "Введите дату выезда:")

        calendar, step = DetailedTelegramCalendar(calendar_id=2,
                                                  min_date=user.arrival_date + (timedelta(days=1)),
                                                  max_date=user.arrival_date + timedelta(days=365),
                                                  locale="ru").build()
        bot.send_message(user.user_id,
                         f"Select {LSTEP[step]}",
                         reply_markup=calendar)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=2))
def handle_departure_date(call):
    user = User.get_user(call.from_user.id)

    result, key, step = DetailedTelegramCalendar(calendar_id=2,
                                                 min_date=user.arrival_date + timedelta(days=1),
                                                 max_date=user.arrival_date + timedelta(days=365),
                                                 locale="ru").process(call.data)
    if not result and key:
        bot.edit_message_text(f"Выберите {LSTEP[step]}",
                              user.user_id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        user.departure_date = result
        bot.send_message(call.message.chat.id, f"\U00002B06 Дата выезда {user.departure_date}")

        bot.delete_message(chat_id=call.message.chat.id,
                           message_id=call.message.message_id)

        bot.delete_message(chat_id=call.message.chat.id,
                           message_id=user.message_to_delete.message_id)

        answer_yes_or_no_button = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton(text='Да',
                                       callback_data='correct_data'),
            types.InlineKeyboardButton(text='Нет',
                                       callback_data='incorrect_data')
        )

        user.nights_number = (user.departure_date - user.arrival_date).days
        bot.send_message(chat_id=call.message.chat.id,
                         text=f'\U000027A1 Время прибывания: {user.nights_number} ночь(ей).')

        bot.send_message(chat_id=call.message.chat.id,
                         text=' Данные указаны верно? ',
                         reply_markup=answer_yes_or_no_button)
