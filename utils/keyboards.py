from telegram import ReplyKeyboardMarkup

def main_menu():
    return ReplyKeyboardMarkup([
        ["🔍 Поиск вакансий"], 
        ["ℹ️ Помощь"]
    ], resize_keyboard=True)
