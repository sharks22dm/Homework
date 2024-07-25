from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from keyboards import *
import texts

API = '6908564813:AAEf1W2jP50L9nKAQTJ4-ZNA1RfvFqsT0fo'
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(texts.start, reply_markup=start_kb)


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост в см')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес в кг')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5
    await message.answer(f'Ваша норма калорий: {calories}', reply_markup=start_kb)
    await state.finish()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=calculate_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(texts.formula)
    await call.answer()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    images = ['img/prod1.jpg', 'img/prod2.jpg', 'img/prod3.jpg', 'img/prod4.jpg']
    descriptions = [texts.product_1, texts.product_2, texts.product_3, texts.product_4]
    for i in range(len(images)):
        with open(images[i], 'rb') as img:
            await message.answer_photo(img, descriptions[i])
    await message.answer('Выберите продукт для покупки', reply_markup=buy_kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
