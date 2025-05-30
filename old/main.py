from telegram.ext import Updater, CommandHandler
from parsers.hh_parser import get_hh_vacancies
import config

def start(update, context):
    update.message.reply_text("🔍 Бот для поиска вакансий для людей с ОВЗ")

def send_jobs_to_channel(context):
    jobs = get_hh_vacancies()
    for job in jobs[:5]:  # Отправляем 5 вакансий
        context.bot.send_message(
            chat_id=config.CHANNEL_ID,
            text=f"🏢 {job['employer']['name']}\n🔹 {job['name']}\n💰 {job.get('salary', 'З/П не указана')}\n🔗 {job['alternate_url']}"
        )

updater = Updater(config.BOT_TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))

# Автопостинг каждые 6 часов
job_queue = updater.job_queue
job_queue.run_repeating(send_jobs_to_channel, interval=21600, first=0)

updater.start_polling()
