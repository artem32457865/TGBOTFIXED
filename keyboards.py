from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from config import COUNTRIES

def countries_kb():
    buttons = [
        [InlineKeyboardButton(text=country, callback_data=f"country_{country}")]
        for country in COUNTRIES.keys()
    ]
    buttons.append([InlineKeyboardButton(text="🌍 Інше місто", callback_data="manual_city")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def cities_kb(country: str):
    buttons = [
        [InlineKeyboardButton(text=city, callback_data=f"city_{city}")]
        for city in COUNTRIES.get(country, [])
    ]
    buttons.append([InlineKeyboardButton(text="⬅️ Назад", callback_data="back")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# Виправлена клавіатура
cancel_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="❌ Скасувати")]],
    resize_keyboard=True
)