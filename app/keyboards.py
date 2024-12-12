from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.users import list_of_todo

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='список задач')],
    [KeyboardButton(text='создать задачу')],
    [KeyboardButton(text='обновить задачу')],
    [KeyboardButton(text='удалить задачу')],
    [KeyboardButton(text='задача по id')],
])

def tasks_kb(user_id):
    tasks = list_of_todo(user_id)
    keyboard = InlineKeyboardBuilder()
    for task_id, task_desc in tasks:
        keyboard.add(InlineKeyboardButton(text=str(task_desc), callback_data=f'task_{task_id}'))
    return keyboard.adjust(2).as_markup()

def get_delete_kb(user_id, task_id):
    return InlineKeyboardMarkup(InlineKeyboardButton(text='Удалить задачу', callback_data=f'rm_{user_id}_{task_id}'))

def get_delete_kb(user_id, task_id):
    return InlineKeyboardBuilder().add(InlineKeyboardButton(text='Удалить задачу', callback_data=f'rm_{user_id}_{task_id}')).adjust(2).as_markup()