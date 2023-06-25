import sys

import flask
import telebot
from flask import Flask, render_template, request, abort
from telebot.types import Update

sys.path.append('/home/m/mggstudia/ecstaticpc/public_html/venv/lib/python3.4/site-packages/')

app = Flask(__name__)
app.debug = True
application = app

# Настройки для Telegram бота
TOKEN = ''
CHAT_ID = ''

bot = telebot.TeleBot(TOKEN)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    # Получаем данные из формы
    name = request.form.get('name')
    phone = request.form.get('phone')

    # Отправка сообщения в чат Telegram
    bot.send_message(CHAT_ID, f"Новая заявка:\nИмя: {name}\nТелефон: {phone}")

    return "все ОК"


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        bot.send_message(CHAT_ID, "Сообщение получено и обработано")
        return 'OK'
    else:
        flask.abort(403)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(CHAT_ID, "ыф")
    bot.reply_to(message,
                 ("Hi there, I am EchoBot.\n"
                  "I am here to echo your kind words back to you."))


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Обработка входящего сообщения
    # Отправка ответного сообщения
    bot.send_message(message.chat.id, "Ваше сообщение получено")


if __name__ == '__main__':
    # Установка вебхука
    bot.remove_webhook()
    bot.set_webhook(url='https://ecstaticpc.ru/webhook')

    app.run()
