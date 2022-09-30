from telebot.types import Message
from loader import bot


@bot.message_handler(commands=['help'])
def bot_help(message: Message) -> None:
    text = '/lowprice - выведу для тебя самые дешевые отели\n' + \
           '/highprice - выведу для тебя самые дорогие отели\n' + \
           '/bestdeal - выведу отели наиболее подходящих по цене и расположению от центра\n' + \
           '/history - выведу историю поиска отелей'
    bot.reply_to(message, text)

