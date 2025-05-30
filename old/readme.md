# 💼 WorkBot for People with Disabilities | Телеграм-бот для поиска работы  

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-✓-green?logo=telegram)](https://core.telegram.org/bots/api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT)

Бот помогает людям с инвалидностью находить вакансии на популярных биржах работы.  
**Актуальные источники**: hh.ru, LinkedIn (адаптированные вакансии), региональные центры занятости.  

---

## ✨ Возможности  
✅ **Умный поиск** с фильтрами:  
- Тип инвалидности (опорно-двигательная, зрение, слух)  
- Удалённая работа  
- Льготные условия  

✅ **Избранное**:  
- Сохранение вакансий  
- Уведомления о новых подходящих позициях  

✅ **Поддержка**:  
- Связь с HR-специалистами  
- Горячие линии трудоустройства  

---

## 🛠 Технологический стек  
| Компонент       | Технологии                          |
|----------------|-----------------------------------|
| Бэкенд         | Python 3.10+, aiogram 3.x         |
| Парсинг        | BeautifulSoup4, aiohttp           |
| База данных    | SQLite (легковесная) / PostgreSQL |
| Деплой         | Docker (опционально)              |

---

## 🚀 Быстрый старт  
### 1. Установка  
```bash
git clone https://github.com/ваш-репозиторий/workbot-disability.git
cd workbot-disability
pip install -r requirements.txt
