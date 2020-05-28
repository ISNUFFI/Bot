from telebot import types
import telebot
import config
bot = telebot.TeleBot(config.token)


def generate_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(types.KeyboardButton('Hello'))


@bot.message_handler(commands=['start'])
def st_message(message):
    generate_markup()
    bot.send_message(message.chat.id, 'Hello!')


@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text, message.chat.first_name)
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['sticker'])
def send_stickid(message):
    print(message)


bot.polling()
