import telebot
from telebot import apihelper
from menu import (
    main_menu,
    vacancy_search_options,
    vacancy_actions,
    back_to_menu
)
from config import BOT_TOKEN

# Настройка логгирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

bot = TeleBot(BOT_TOKEN)

# Удаляем вебхук перед запуском
try:
    bot.delete_webhook()
except Exception as e:
    print(f"Ошибка при удалении вебхука: {e}")

# Затем запускаем поллинг
bot.polling(none_stop=True)

# /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: types.Message):
    user = message.from_user
    bot.send_message(
        message.chat.id,
        f"👋 Привет, {user.first_name}! Я помогу найти работу для людей с инвалидностью.\n"
        "Выберите действие в меню:",
        reply_markup=main_menu()
    )
    logger.info(f"User {user.id} started the bot")

# Главное меню
@bot.message_handler(func=lambda msg: msg.text == '⬅️ Назад')
def back_handler(message: types.Message):
    bot.send_message(
        message.chat.id,
        "Главное меню:",
        reply_markup=main_menu()
    )

# Поиск вакансий
@bot.message_handler(func=lambda msg: msg.text == '🔍 Поиск вакансий')
def search_vacancies(message: types.Message):
    bot.send_message(
        message.chat.id,
        "🔎 Введите ключевые слова (например, 'удалённая работа'):",
        reply_markup=back_to_menu()
    )
    bot.register_next_step_handler(message, process_search_query)

def process_search_query(message: types.Message):
    query = message.text
    # Здесь будет вызов парсера (заглушка)
    bot.send_message(
        message.chat.id,
        f"🔍 Ищу вакансии по запросу: '{query}'...",
        reply_markup=vacancy_actions(vacancy_id=1)  # Пример ID вакансии
    )
    logger.info(f"Search: {query}")

# Настройки фильтров
@bot.message_handler(func=lambda msg: msg.text == '⚙️ Настройки поиска')
def show_filters(message: types.Message):
    bot.send_message(
        message.chat.id,
        "⚙️ Выберите тип фильтра:",
        reply_markup=vacancy_search_options()
    )

# Обработка callback-ов (фильтры, действия с вакансиями)
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call: types.CallbackQuery):
    if call.data.startswith('filter_'):
        filter_type = call.data.split('_')[1]
        bot.answer_callback_query(
            call.id,
            f"Применён фильтр: {filter_type}"
        )
        # Здесь будет логика фильтрации
    elif call.data.startswith('save_'):
        vacancy_id = call.data.split('_')[1]
        bot.answer_callback_query(
            call.id,
            "✅ Вакансия сохранена в избранное"
        )
    elif call.data == 'next_vacancy':
        # Заглушка - в реальности подгружаем следующую вакансию
        bot.edit_message_text(
            "Следующая вакансия:\n\n<b>Удалённый оператор</b>\nЗарплата: 30 000 руб.",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=vacancy_actions(vacancy_id=2),
            parse_mode='HTML'
        )

# Запуск бота
if __name__ == '__main__':
    logger.info("Bot started")
    bot.infinity_polling()
