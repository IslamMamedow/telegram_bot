from telebot import TeleBot
from config_data import config
from peewee import *

bot = TeleBot(token=config.bot_token)
rapid_key = config.rapid_api_key

database = SqliteDatabase('history.db')

