from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    """Главное меню бота"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    btn1 = KeyboardButton("🔍 Поиск вакансий")
    btn2 = KeyboardButton("⚙️ Настройки поиска")
    btn3 = KeyboardButton("📌 Избранные вакансии")
    btn4 = KeyboardButton("ℹ️ Информация о боте")
    btn5 = KeyboardButton("📞 Связь с поддержкой")
    
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup


def vacancy_search_options():
    """Меню настроек поиска (фильтры)"""
    markup = InlineKeyboardMarkup(row_width=2)
    
    btn1 = InlineKeyboardButton("Удалённая работа", callback_data="filter_remote")
    btn2 = InlineKeyboardButton("Для колясочников", callback_data="filter_wheelchair")
    btn3 = InlineKeyboardButton("Для слабовидящих", callback_data="filter_vision")
    btn4 = InlineKeyboardButton("Сбросить фильтры", callback_data="filter_reset")
    
    markup.add(btn1, btn2, btn3, btn4)
    return markup


def vacancy_actions(vacancy_id):
    """Кнопки для взаимодействия с вакансией (сохранить, поделиться и т. д.)"""
    markup = InlineKeyboardMarkup()
    
    btn1 = InlineKeyboardButton("💾 Сохранить", callback_data=f"save_{vacancy_id}")
    btn2 = InlineKeyboardButton("📤 Поделиться", callback_data=f"share_{vacancy_id}")
    btn3 = InlineKeyboardButton("➡️ Следующая", callback_data=f"next_vacancy")
    
    markup.add(btn1, btn2, btn3)
    return markup


def back_to_menu():
    """Кнопка 'Назад'"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("⬅️ Назад"))
    return markup
