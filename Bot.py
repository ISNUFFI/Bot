import telebot
import config
bot = telebot.TeleBot(config.token)


Button1 = telebot.types.KeyboardButton('Throw the dice')
telebot.types.ReplyKeyboardMarkup(Button1, True)

@bot.message_handler(commands=['start'])
def st_message(message):
    bot.send_message(message.chat.id, 'Hello World!')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAP_Xs_rg-rzFzCJK46JaqHmwjcWjNIAAk0cAAIkhhQFBVasJEbr6z8ZBA')

@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text, message.chat.first_name)
    bot.send_message(message.chat.id, message.text)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBjF7P7AOoo4vgRL2KlUKtbd7y4YwtAAJVAQAC81Y_F3TXHEt6LzP4GQQ')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBrl7P89Jj4gHDo1g1HvjkpjmQ5CpmAAIgAAONAAHOMadDuA1w4KC4GQQ')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBql7P83NJ-oYmQHd6yoQpM3ycGiezAAJVAQAC81Y_F3TXHEt6LzP4GQQ')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBqV7P82i5W7t1Q8w_yXzEqXdIwM5PAAKFAQACmZhGEZ4-vwN_gxrlGQQ')

@bot.message_handler(content_types=['sticker'])
def send_stickid(message):
    print(message)

bot.polling()