
from loader import bot
from states.user import User
from keyboard import bot_calendar, choose_number_of_photo
from handlers import find_hotel
from handlers import set_hotel_price_range_and_distance
from handlers import print_hotel


@bot.callback_query_handler(func=lambda call: True)
def inline_answer(call):
    """Функция обрабатывает нажатие inline-кнопок пользователем """

    user = User.get_user(user_id=call.from_user.id)

    # --------------------для получения следующего отеля
    if call.data == 'next_hotel':
        if user.hotels_count > len(user.hotels_list) - 1:
            bot.send_message(chat_id=call.message.chat.id,
                             text='\U0000203C	Отели по вашему запросу закончились!')
        else:
            print_hotel.print_hotel_and_photo(message=user.message,
                                              hotel=user.hotels_list[user.hotels_count])

    # ---------------------подтверждения корректных данных после введения даты прибывания
    elif call.data == 'correct_data':
        if user.command == '/bestdeal':
            set_hotel_price_range_and_distance.set_price_range(user.message)

        elif user.command == '/lowprice' or user.command == '/highprice':
            choose_number_of_photo.show_or_not_show_photo(message=user.message)

    elif call.data == 'incorrect_data':
        bot_calendar.set_arrival_date(message=user.message)

    # ---------------------установка надобности фото при выведении отелей
    elif call.data == 'with_photo':
        user.show_photo = True
        choose_number_of_photo.choice_number(message=user.message)
    elif call.data == 'without_photo':
        find_hotel.get_hotel_list(message=user.message)

    # ---------------------установка количества выводимый фото
    elif call.data[:2] == 'ch':
        user.number_of_photo = int(call.data[2:])
        find_hotel.get_hotel_list(message=user.message)

    # ---------------------для повторного введения города для поиска
    elif call.data == 'try_again':
        message_from_user = bot.send_message(chat_id=call.message.chat.id,
                                             text='\U0001F30F	Укажите город:')
        bot.register_next_step_handler(message=message_from_user,
                                       callback=find_hotel.search_city)

    # -------------------подтверждение корректных данных после ввода диапазона цен
    elif call.data == 'center_correct_data':
        set_hotel_price_range_and_distance.get_max_distance_from_center(user.message)
    elif call.data == 'center_incorrect_data':
        set_hotel_price_range_and_distance.set_price_range(user.message)

    # ---------------------выбор искомой локации
    elif user.command == '/lowprice' or user.command == '/highprice' or user.command == '/bestdeal':
        user.location_id = call.data
        user.location = user.location_id_with_locations_name[call.data]

        bot.send_message(chat_id=call.message.chat.id,
                         text=f'Вы выбрали:\n      \U00002708 {user.location}')
        bot.delete_message(chat_id=call.message.chat.id,
                           message_id=user.message_to_delete.message_id)
        bot_calendar.set_arrival_date(message=user.message)
