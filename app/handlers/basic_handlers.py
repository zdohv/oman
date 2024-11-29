from aiogram import types, Router, F
from aiogram.filters import Command


router = Router()

@router. message(Command('start'))
async def start(message: types.Message):
    await message.answer('oma коток пидарас жетим сучка чурка')

#TODO - написать оброботчик /help - отправляет два сообщения: 1. "инструкция по тспользонию бота",2.
