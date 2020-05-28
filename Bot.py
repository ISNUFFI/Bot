from telebot import types
from random import randint
import telebot
import config
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


bot.polling()
