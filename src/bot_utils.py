import os
import requests
from dotenv import load_dotenv
from properties.config import CHAT_ID

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

def get_telegram_bot_url(token):
  return "https://api.telegram.org/bot{}/".format(token)

def get_telegram_send_message_url(token, text, chat_id):
  return '{}sendMessage?text={}&chat_id={}'.format(get_telegram_bot_url(token), text, chat_id)

def get_telegram_get_updates_url(token):
  return '{}getUpdates'.format(get_telegram_bot_url(token))

def send_telegram_message(text):
  url = get_telegram_send_message_url(
    token=TOKEN,
    text=text,
    chat_id=CHAT_ID
  )
  response = requests.get(url)
  content = response.content.decode("utf8")
  print('Message sent:', text)
  return content
