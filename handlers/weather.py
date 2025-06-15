
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import config
from keyboards import countries_kb, cities_kb, cancel_kb
from services.weather_api import WeatherAPI

router = Router()

class States(StatesGroup):
    waiting_city = State()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Вітаю! Я бот погоди. Оберіть країну:",
        reply_markup=countries_kb()
    )

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "🛠 Доступні команди:\n"
        "/start — Запустити бота\n"
        "/help — Допомога / список команд\n\n"
        "Або просто оберіть країну і місто з меню ⬇️"
    )

@router.callback_query(F.data.startswith("country_"))
async def country_selected(callback: types.CallbackQuery):
    country = callback.data.split("_", 1)[1]
    await callback.message.edit_text(
        f"Оберіть місто в {country}:",
        reply_markup=cities_kb(country)
    )
    await callback.answer()

@router.callback_query(F.data.startswith("city_"))
async def city_selected(callback: types.CallbackQuery):
    city = callback.data.split("_", 1)[1]
    weather_data = await WeatherAPI.get_weather(city)

    if weather_data:
        await callback.message.edit_text(
            WeatherAPI.format_weather(weather_data),
            reply_markup=countries_kb()
        )
    else:
        await callback.message.edit_text(
            "Не вдалося отримати дані про погоду",
            reply_markup=countries_kb()
        )
    await callback.answer()

@router.callback_query(F.data == "manual_city")
async def manual_city(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        "Введіть назву міста (на англійській мові з великої букви. наприклад: Berlin):"
    )
    await state.set_state(States.waiting_city)
    await callback.answer()

@router.message(States.waiting_city, F.text == "❌ Скасувати")
async def cancel_input(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Оберіть країну:",
        reply_markup=countries_kb(),
        reply_markup_remove=True
    )

@router.message(States.waiting_city)
async def city_entered(message: types.Message, state: FSMContext):
    weather_data = await WeatherAPI.get_weather(message.text)

    if weather_data:
        await message.answer(
            WeatherAPI.format_weather(weather_data),
            reply_markup=countries_kb()
        )
        await state.clear()
    else:
        await message.answer(
            "Місто не знайдено. Спробуйте ще раз:",
            reply_markup=cancel_kb
        )

@router.callback_query(F.data == "back")
async def back_to_countries(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Оберіть країну:",
        reply_markup=countries_kb()
    )
    await callback.answer()
