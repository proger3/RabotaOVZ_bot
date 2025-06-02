import logging
from telebot import TeleBot, types
from menu import main_menu

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

bot = TeleBot("7861669024:AAFKFY1TR_ZE_kmn-nv9D9onQgSM7k-LS7E")  # Замените на ваш токен

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    try:
        user = message.from_user
        logger.info(f"Пользователь {user.id} запустил бота")
        
        bot.send_message(
            message.chat.id,
            f"👋 Привет, {user.first_name}! Я помогу найти работу для людей с инвалидностью.\n"
            "Выберите действие в меню:",
            reply_markup=main_menu()
        )
    except Exception as e:
        logger.error(f"Ошибка в send_welcome: {e}")

@bot.message_handler(func=lambda message: message.text == '🔍 Поиск вакансий')
def search_vacancies(message):
    try:
        msg = bot.send_message(
            message.chat.id,
            "🔎 Введите ключевые слова (например, 'удалённая работа'):",
            reply_markup=types.ReplyKeyboardRemove()
        )
        bot.register_next_step_handler(msg, process_search_query)
    except Exception as e:
        logger.error(f"Ошибка в search_vacancies: {e}")

def process_search_query(message):
    try:
        query = message.text
        logger.info(f"Поиск по запросу: {query}")
        
        # Здесь будет логика поиска вакансий
        bot.send_message(
            message.chat.id,
            f"🔍 Ищу вакансии по запросу: '{query}'...",
            reply_markup=main_menu()
        )
    except Exception as e:
        logger.error(f"Ошибка в process_search_query: {e}")

@bot.message_handler(func=lambda message: message.text == '⬅️ Назад')
def back_to_menu(message):
    try:
        bot.send_message(
            message.chat.id,
            "Главное меню:",
            reply_markup=main_menu()
        )
    except Exception as e:
        logger.error(f"Ошибка в back_to_menu: {e}")

if __name__ == '__main__':
    logger.info("Бот запускается...")
    try:
        # Удаляем вебхук перед запуском polling
        bot.delete_webhook()
        logger.info("Webhook удален, запускаем polling...")
        
        bot.polling(none_stop=True, interval=2)
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
    finally:
        logger.info("Бот остановлен")
