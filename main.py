from loader import bot
import handlers
from database.model import create_db

if __name__ == '__main__':
    create_db()
    bot.infinity_polling()
