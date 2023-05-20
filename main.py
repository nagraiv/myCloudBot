import telebot
import os


bot = telebot.TeleBot(os.environ['TOKEN'])

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Вас приветствует эхо бот!')


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)

