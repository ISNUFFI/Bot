from telebot import types
import random
import telebot
import config
bot = telebot.TeleBot(config.token)

keyboard1 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard1.row('Кинуть кости')


@bot.message_handler(commands=['start'])
def st_message(message):
    bot.send_message(message.chat.id, 'Hello!', reply_markup=keyboard1)
    print(message.chat.first_name)


@bot.message_handler(commands=['dice'])
def dicethrow_message(message):
    bot.send_message(str(random.randint(1, 6)))
    print('dice', message.chat.first_name)


@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text, message.chat.first_name)


bot.polling()
