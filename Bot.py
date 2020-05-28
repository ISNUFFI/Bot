from telebot import types
import telebot
import config
bot = telebot.TeleBot(config.token)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')


@bot.message_handler(commands=['start'])
def st_message(message):
    bot.send_message(message.chat.id, 'Hello!')
    print(message.chat.first_name)


@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text, message.chat.first_name)
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['sticker'])
def send_stickid(message):
    print(message)


bot.polling()
