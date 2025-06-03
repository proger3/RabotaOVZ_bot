import requests

TOKEN = "ВАШ_ТОКЕН"  # Замените на реальный токен
VERCEL_URL = "https://ваш-проект.vercel.app/api"  # Ваш URL из Vercel

# Удаляем старый вебхук
requests.get(f"https://api.telegram.org/bot{TOKEN}/deleteWebhook")

# Устанавливаем новый
response = requests.get(
    f"https://api.telegram.org/bot{TOKEN}/setWebhook",
    params={"url": VERCEL_URL}
)

print(response.json())  # Должен показать {"ok":true,"result":true}
