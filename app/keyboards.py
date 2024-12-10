from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='список задач')],
    [KeyboardButton(text='создать задач')],
    [KeyboardButton(text='обновить задач')],
    [KeyboardButton(text='удалить задач')],
    [KeyboardButton(text='задача по id')],
])