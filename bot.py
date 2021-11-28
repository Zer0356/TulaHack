import telebot

bot = telebot.TeleBot("2136192507:AAGx1pQUEZAUPNZxFpo8RoPlEOde7AmDnYk")

@bot.message_handler(content_types=['text'])
def main(message):
    if message.chat.type == "private":
        if message.text == "Привет":
            bot.send_message(message.chat.id, "Привет")

bot.polling()