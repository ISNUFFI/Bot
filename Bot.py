from telebot import types
from random import randint
import telebot
import config
import os
import time
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('C:/Users/SNUFF/Pictures/tg'):
        f = open('C:/Users/SNUFF/Pictures/tg'+file, 'rb')
        msg = bot.send_photo(message.chat.id, f, None)
        # А теперь отправим вслед за файлом его file_id
        bot.send_message(message.chat.id, msg.photo.file_id, reply_to_message_id=msg.message_id)
    time.sleep(3)


bot.polling()
