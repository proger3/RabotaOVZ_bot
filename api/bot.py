from http.server import BaseHTTPRequestHandler
import json
from telebot import TeleBot
from menu import main_menu  # Импорт вашего меню

bot = TeleBot("7861669024:AAFKFY1TR_ZE_kmn-nv9D9onQgSM7k-LS7E")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=main_menu())

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        update = json.loads(post_data.decode('utf-8'))
        bot.process_new_updates([update])
        self.send_response(200)
        self.end_headers()
