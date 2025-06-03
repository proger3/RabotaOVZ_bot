from http.server import BaseHTTPRequestHandler
import json
import logging
from telebot import TeleBot
import os
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = TeleBot(os.getenv('BOT_TOKEN'))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Бот работает! ✅")

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            update = json.loads(post_data.decode('utf-8'))
            bot.process_new_updates([update])
        except Exception as e:
            logger.error(f"Error processing update: {e}")
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

def endpoint(request):
    handler = Handler(request)
    handler.handle_request()
    return handler
