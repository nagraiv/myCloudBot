import telebot
from telebot import types
import os


bot = telebot.TeleBot(os.environ['TOKEN'])


def keyboard():
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Наш сайт', url='https://habrahabr.ru')
    markup.add(btn_my_site)
    return markup


@bot.message_handler(commands=["help"])
def show_help(message):
    bot.send_message(message.chat.id, 'Я эхо бот. Я умею только отвечать в точности то, что вы мне написали.')


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Вас приветствует эхо бот!', reply_markup=keyboard())


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)

