# -*- coding: utf-8 -*-
import redis
import os
import telebot
from handler import stopnum
from telebot import types

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

bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
stopdict = {}
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, what stop would you like to know the last bus times for?")

@bot.message_handler(func=lambda m: True)
def respond_all(message):
    print(message.text)
    if message.text.isdigit():
        stop = stopnum(message.text)
        stopdict[message.chat.id] = stop
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Weekdays')
        itembtn2 = types.KeyboardButton('Saturdays')
        itembtn3 = types.KeyboardButton('Sundays')
        markup.add(itembtn1, itembtn2, itembtn3)
        msg = bot.reply_to(message, "Choose a Day", reply_markup=markup)
        bot.register_next_step_handler(msg, day_step)
    else:
        bot.send_message(message.chat.id, "Sorry, I can't understand that yet! Send me a bus stop code.")

def day_step(message):
    dayind = {"Weekdays":0, "Saturdays":1, "Sundays":2}[message.text]
    text = stopdict[message.chat.id]
    res = text.times(dayind)
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, res,reply_markup=markup)
    

"""
@bot.message_handler(func=lambda m: True)
def respond_all(message):
    print(message.text)
    text = s1.time(message.text)
    if text:
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "Sorry, I can't understand that yet!")
"""
bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling()
