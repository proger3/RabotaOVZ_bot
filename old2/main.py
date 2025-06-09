import os
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

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    logger.error("Не задан BOT_TOKEN!")
    exit(1)

bot = TeleBot(BOT_TOKEN)
app = Flask(__name__)

# Обработчики команд
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    try:
        user = message.from_user
        logger.info(f"Новый пользователь: {user.id}")
        
        # Новый текст с разделением на соискателей и работодателей
        welcome_text = f"""
👋 *Привет, {user.first_name}!* Я бот @rabotaOVZ_bot — помогаю людям с инвалидностью найти работу, а компаниям — ответственных сотрудников.

🔹 *Для соискателей:*
- Ищу вакансии с пандусами/лифтами 🦽
- Подбираю удалённую работу 🏠
- Учитываю ваш тип инвалидности
👉 Нажмите /search чтобы начать

🔹 *Для работодателей:*
- Размещайте инклюзивные вакансии бесплатно
- Получите проверенных кандидатов
👉 Нажмите /hr для инструкций

📌 *Полезное:*
/help — все команды
/legal — права при трудоустройстве
"""
        bot.send_message(
            message.chat.id,
            welcome_text,
            parse_mode="Markdown",  # Для жирного текста (* *)
            reply_markup=main_menu()  # Ваши кнопки остаются
        )
    except Exception as e:
        logger.error(f"Ошибка в send_welcome: {e}")
        bot.send_message(message.chat.id, "⚠️ Ошибка. Попробуйте позже.")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        if message.text == '🔍 Поиск вакансий':
            msg = bot.send_message(
                message.chat.id,
                "🔎 Введите ключевые слова для поиска:",
                reply_markup=types.ReplyKeyboardRemove()
            )
            bot.register_next_step_handler(msg, process_search)
        elif message.text == '⬅️ Назад':
            bot.send_message(
                message.chat.id,
                "Главное меню:",
                reply_markup=main_menu()
            )
    except Exception as e:
        logger.error(f"Ошибка обработки сообщения: {e}")

def process_search(message):
    try:
        query = message.text
        logger.info(f"Поиск: {query}")
        # Здесь будет логика поиска
        bot.send_message(
            message.chat.id,
            f"🔍 Ищем вакансии по запросу: '{query}'...",
            reply_markup=main_menu()
        )
    except Exception as e:
        logger.error(f"Ошибка поиска: {e}")

# Вебхук обработчик
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_data = request.get_data().decode('utf-8')
        update = types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return '', 200
    return 'Bad request', 400

if __name__ == '__main__':
    try:
        # Получаем URL вебхука из переменных окружения
        WEBHOOK_URL = os.getenv('WEBHOOK_URL')
        if not WEBHOOK_URL:
            logger.error("Не задан WEBHOOK_URL!")
            exit(1)

        logger.info("Устанавливаем вебхук...")
        bot.remove_webhook()
        bot.set_webhook(url=f"{WEBHOOK_URL}/webhook")
        
        logger.info("Бот запущен в режиме вебхука")
        app.run(host='0.0.0.0', port=10000)
    except Exception as e:
        logger.error(f"Фатальная ошибка: {e}")
