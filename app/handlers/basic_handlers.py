from aiogram import types, Router, F 
from aiogram.filters import Command 
 
from app.keyboards import main_kb
router = Router() 
 
@router.message(Command('start')) 
async def start(message: types.Message): 
    await message.answer("oma pidr", reply_markup=main_kb) 
 
@router.message(Command('help')) 
async def help_command(message: types.Message): 
    first_message = ('инструкция по тспользонию бота') 
    await message.answer(first_message) 
 
    second_message = ("Бот позволяет управлять задачами с помощью кнопок. Вот доступные функции /n 1. Список задач /n Показывает список всех ваших задач с их ID. Используйте ID для работы с конкретной задачей.  /n 2. Конкретная задача  /n Выберите задачу по ID, чтобы увидеть ее описание и дату выполнения. /n 3. Создание задачи  /n Позволяет добавить новую задачу. Бот запросит описание и дату выполнения.  /n 4.Удаление задачи  /n Удаляет задачу по ID. Просто выберите задачу из списка для удаления. /n 5. Обновление задачи /n Позволяет изменить описание или дату выполнения выбранной задачи.") 
    await message.answer(second_message) 