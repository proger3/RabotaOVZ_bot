from http.server import BaseHTTPRequestHandler
from telebot import TeleBot
import json

bot = TeleBot(os.getenv('BOT_TOKEN'))

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
