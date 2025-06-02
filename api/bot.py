from http.server import BaseHTTPRequestHandler
import json
from telebot import TeleBot

bot = TeleBot("ВАШ_ТОКЕН")

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        update = json.loads(post_data.decode('utf-8'))
        
        if 'message' in update:
            chat_id = update['message']['chat']['id']
            bot.send_message(chat_id, "Бот работает на Vercel!")
        
        self.send_response(200)
        self.end_headers()

def endpoint(request):
    handler = Handler(request)
    handler.handle_request()
    return handler
