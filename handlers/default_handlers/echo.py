from telebot.types import Message
from loader import bot


@bot.message_handler(content_types=['text'])
def bot_echo(message: Message):
    if message.text == '/hello-world':
        bot.reply_to(message=message,
                     text='Привет Мир!!!')
    elif message.text == 'Привет':
        bot.reply_to(message=message,
                     text='Привет!\n'
                          'Я помогу тебе с выбором отеля\n'
                          'Просмотреть что я могу введи:\n/help')
    else:
        bot.reply_to(message, "Эхо без состояния или фильтра.\nСообщение: "
                              f"{message.text}\n"
                              "Введите команду /help")
