from telebot import types
from random import randint
import telebot
import config
import os
import time
bot = telebot.TeleBot(config.token)

keyboard1 = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
keyboard1.row('Кинуть кости {}'.format(config.dice))


@bot.message_handler(commands=['start'])
def st_message(message):
    bot.send_message(message.chat.id, 'Hello!', reply_markup=keyboard1)
    print(message.chat.first_name)


@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text, message.chat.first_name)
    if message.text.lower() == 'кинуть кости {}'.format(config.dice):
        rnd = randint(1, 6)
        bot.send_message(message.chat.id, config.dices[rnd])


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('C:/Users/SNUFF/Pictures/tg'):
        f = open('C:/Users/SNUFF/Pictures/tg'+file, 'rb')
        msg = bot.send_photo(message.chat.id, f, None)
        # А теперь отправим вслед за файлом его file_id
        bot.send_message(message.chat.id, msg.photo.file_id, reply_to_message_id=msg.message_id)
    time.sleep(3)


bot.polling()
