from telebot import types
import telebot
import config
bot = telebot.TeleBot(config.token)





@bot.message_handler(commands=['start'])
def st_message(message):
    bot.send_message(message.chat.id, 'Hello!')
    print(message.chat.first_name)
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    button_phone = types.KeyboardButton(text="", request_contact=True)
    user_markup.add(button_phone)
    send = bot.send_message(message.chat.id, 'Поделитесь своим номером',reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text, message.chat.first_name)
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['sticker'])
def send_stickid(message):
    print(message)


bot.polling()
