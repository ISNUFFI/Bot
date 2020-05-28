import telebot
import config
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def st_message(message):
    bot.send_message(message.chat.id, 'Hello World!')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAP_Xs_rg-rzFzCJK46JaqHmwjcWjNIAAk0cAAIkhhQFBVasJEbr6z8ZBA')


@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text, message.chat.first_name)
    bot.send_message(message.chat.id, message.text)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBjF7P7AOoo4vgRL2KlUKtbd7y4YwtAAJVAQAC81Y_F3TXHEt6LzP4GQQ')
    if message.text.lower() == 'dice' :
        bot.get_user_profile_photos(message.chat.id)


@bot.message_handler(content_types=['sticker'])
def send_stickid(message):
    print(message)


bot.polling()