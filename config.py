import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

ADMIN_IDS = [651916072]  # ID админов для уведомлений
