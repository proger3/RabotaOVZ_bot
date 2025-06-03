from flask import Flask, request
from telebot import TeleBot, types
import os

app = Flask(__name__)
bot = TeleBot(os.getenv('BOT_TOKEN'))

# Создаём меню
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔍 Поиск вакансий')
    btn2 = types.KeyboardButton('ℹ️ Помощь')
    markup.add(btn1, btn2)
    return markup

# Обработчики команд
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать! Выберите действие:",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda m: m.text == '🔍 Поиск вакансий')
def search_vacancies(message):
    bot.send_message(message.chat.id, "Введите профессию для поиска:")

@bot.message_handler(func=lambda m: m.text == 'ℹ️ Помощь')
def show_help(message):
    bot.send_message(message.chat.id, "Этот бот помогает найти работу.")

# Вебхук
@app.route('/api', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        update = types.Update.de_json(request.get_data().decode('utf-8'))
        bot.process_new_updates([update])
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
