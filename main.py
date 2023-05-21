import telebot
from telebot import types
import os

from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP


bot = telebot.TeleBot(os.environ['TOKEN'])


@bot.message_handler(commands=['date'])
def choose_date(m):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(m.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(c):
    result, key, step = DetailedTelegramCalendar().process(c.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"You selected {result}",
                              c.message.chat.id,
                              c.message.message_id)


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

