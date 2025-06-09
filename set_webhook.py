import requests

TOKEN = BOT_TOKEN  # Замените на реальный токен
VERCEL_URL = https://vercel.com/proger3s-projects/rabota-ovz-bot  # Ваш URL из Vercel

# Удаляем старый вебхук
requests.get(f"https://api.telegram.org/bot{TOKEN}/deleteWebhook")

# Устанавливаем новый
response = requests.get(
    f"https://api.telegram.org/bot{TOKEN}/setWebhook",
    params={"url": VERCEL_URL}
)

print(response.json())  # Должен показать {"ok":true,"result":true}
