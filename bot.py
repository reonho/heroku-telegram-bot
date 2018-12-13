# -*- coding: utf-8 -*-
import redis
import os
import telebot
from sheethandler import sheethandler
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
#some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
r = redis.from_url(os.environ.get("REDIS_URL"))
#       Your bot code below

s1 = sheethandler()
bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, which station would you like to know the last train time for? (Give me a station name)")

@bot.message_handler(func=lambda m: True)
def respond_all(message):
    print(message.text)
    text = s1.time(message.text)
    if text:
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "Sorry, I don't understand. Give me a station name!")

bot.polling()
