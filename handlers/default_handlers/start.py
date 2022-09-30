from telebot.types import Message
from loader import bot
from states.user import User
from handlers import find_hotel, history


@bot.message_handler(commands=['start', 'lowprice', 'highprice', 'bestdeal', 'history'])
def bot_start(message: Message) -> None:
    user = User(message.from_user.id)
    user.message = message

    if message.text == '/lowprice' or message.text == '/highprice' or message.text == '/bestdeal':
        user.command = message.text
        bot.send_message(chat_id=message.chat.id,
                         text='\U0001F30F	Укажите город:')
        bot.register_next_step_handler(message=message,
                                       callback=find_hotel.search_city)

    elif message.text == '/history':
        history.print_history(message=message)

    elif message.text == '/start':
        bot.send_sticker(chat_id=message.chat.id,
                         sticker='CAACAgIAAxkBAAEFy49jHJdzeT4AAWHxNv3Ruowa5S0tQoAAAlQAA0G1Vgxqt_jHCI0B-ikE',
                         timeout=5)
        bot.reply_to(message, f'Привет,{message.from_user.full_name}\n'
                              f'Я бот {bot.get_me().full_name} помогу тебе в поиске отелей\n'
                              'Увидеть все команды введи /help')
