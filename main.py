import logging
from flask import Flask, request
from telebot import TeleBot, types
from menu import main_menu

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
bot = TeleBot("ВАШ_ТОКЕН")  # Замените на реальный токен

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    try:
        user = message.from_user
        logger.info(f"Пользователь {user.id} запустил бота")
        bot.send_message(
            message.chat.id,
            f"👋 Привет, {user.first_name}! Я бот для поиска работы.\nВыберите действие:",
            reply_markup=main_menu()
        )
    except Exception as e:
        logger.error(f"Ошибка в send_welcome: {e}")

@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_data = request.get_data().decode('utf-8')
        update = types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return ''
    return 'Bad request', 400

if __name__ == '__main__':
    logger.info("Удаляем старый вебхук...")
    bot.remove_webhook()
    
    # Установите ваш реальный URL Render
    webhook_url = "https://your-render-service.onrender.com"
    logger.info(f"Устанавливаем вебхук на {webhook_url}")
    bot.set_webhook(url=webhook_url)
    
    logger.info("Запускаем Flask сервер...")
    app.run(host='0.0.0.0', port=10000)
