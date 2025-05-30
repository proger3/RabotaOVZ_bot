# 🤖 RabotOVZ_bot  
Telegram-бот для поиска вакансий для людей с ОВЗ  

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot_API-green)](https://core.telegram.org/bots/api)

Бот парсит вакансии с HH.ru и других платформ, фильтрует их для людей с инвалидностью и публикует в Telegram-канал.  

---

## 📌 Возможности  
- Автоматический сбор вакансий с пометкой «для инвалидов».  
- Фильтрация по удалённой работе и типу занятости.  
- Ежедневная отправка подборки в Telegram-канал.  

---

## ⚙️ Установка  
1. Клонируйте репозиторий:  
  
   git clone https://github.com/ваш_логин/RabotOVZ_bot.git
   cd RabotOVZ_bot
   
 

2. Установите зависимости:  
  
   pip install -r requirements.txt
   
 

3. Настройте конфиг:  
   Создайте файл config.py и добавьте:  
  
   BOT_TOKEN = "ВАШ_ТОКЕН_БОТА"
   CHANNEL_ID = "@ваш_канал"  # Или ID чата
   
 

4. Запустите бота:  
  
   python main.py
   
 

---

## 📂 Структура проекта  
RabotOVZ_bot/
├── main.py             # Главный скрипт бота
├── parsers/            # Парсеры вакансий
├── database/           # База данных SQLite
├── utils/              # Вспомогательные скрипты
└── README.md           # Этот файл
 

---

## 🔧 Технологии  
- Python 3.8+  
- Библиотеки: python-telegram-bot, requests, sqlite3  
- API: HH.ru, Trudvsem  

---

## 🤝 Как помочь проекту?  
- Предложите новые источники вакансий.  
- Добавьте фильтры по типу инвалидности.  
- Улучшите дизайн сообщений бота.  

---

## 📜 Лицензия  
MIT License.
