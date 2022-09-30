import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены, установите файл .env по шаблону .env.template')
else:
    load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
rapid_api_key = os.getenv('RAPID_API_KEY')
