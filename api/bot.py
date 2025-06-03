from http.server import BaseHTTPRequestHandler
import os  # Добавьте эту строку
from telebot import TeleBot
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
bot = TeleBot(os.getenv('BOT_TOKEN'))

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            logger.info(f"Received data: {post_data.decode()}")  # Логируем входящий запрос
            
            update = json.loads(post_data.decode('utf-8'))
            bot.process_new_updates([update])
            
        except Exception as e:
            logger.error(f"Error: {str(e)}", exc_info=True)  # Логируем полную трассировку ошибки
        
        self.send_response(200)
        self.end_headers()
# Обработчики команд бота
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Бот работает!")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):  # Обработка GET-запросов (для проверки работоспособности)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Telegram Bot is running!')
    
    def do_POST(self):  # Основной обработчик вебхука
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        update = json.loads(post_data.decode('utf-8'))
        bot.process_new_updates([update])
        self.send_response(200)
        self.end_headers()

def endpoint(request):
    handler = Handler(request)
    handler.handle_request()
    return handler
