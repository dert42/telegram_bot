import time

from bot import bot
from parser import parse


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добрый день. Как вас зовут?")


@bot.message_handler(content_types='text')
def response(message):
    dollar_exchange_rate = parse()
    bot.send_message(message.chat.id, f'Рад знакомству, <b>{message.text}</b>! '
                                      f'Курс доллара сегодня {dollar_exchange_rate}', parse_mode='html')


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)
