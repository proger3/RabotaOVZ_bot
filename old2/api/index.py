from http.server import BaseHTTPRequestHandler
from telebot import TeleBot
import json

bot = TeleBot("7861669024:AAFKFY1TR_ZE_kmn-nv9D9onQgSM7k-LS7E")

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        update = json.loads(post_data.decode('utf-8'))
        
        # Обработка сообщений
        if 'message' in update:
            chat_id = update['message']['chat']['id']
            bot.send_message(chat_id, "Привет! Я работаю на Vercel!")
        
        self.send_response(200)
        self.end_headers()

def vercel_handler(request):
    handler = Handler(request)
    handler.handle_request()
    return handler
