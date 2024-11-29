import sys
import os
import re
from datetime import datetime
from dataclasses import asdict

from repositories.schemas import BaseTask


# Добавляем корневую директорию в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def to_dict(task: BaseTask) -> dict:
    '''Сериализовать объект Task в словарь.'''
    return asdict(task)


def from_input_to_object_task(
    task_id: int,
    title: str,
    description: str,
    category: str,
    due_date: str,
    priority: str
) -> BaseTask:
    '''Создать объект Task из входных параметров.'''
    
    return BaseTask(
        task_id=task_id,
        title=title.capitalize(),
        description=description.capitalize(),
        category=category.capitalize(),
        due_date=due_date,
        priority=priority.capitalize(),
    )

def check_category_name(category_name: str) -> bool:
    '''Проверить корректность ввода имени категории.'''
    
    categories = ['Личное', 'Обучение', 'Работа']
    if category_name.capitalize() in categories:
        return True
    else:
        return False
    
def check_task(title: str, category: str, due_date: str, priority: str) -> bool:
    '''Проверить корректность ввода задачи.'''
    
    if re.sub(r'\D', '', due_date).isdigit():
        try:
            # Преобразуем строку в объект даты
            user_date = datetime.strptime(due_date, "%d.%m.%Y").date()
            current_date = datetime.now().date()  # Получаем текущую дату без времени
            
        except ValueError:
            print(f"Некорректная дата: {due_date}")
            return False
    
    if not title or not category or not due_date or not priority:
        return False
    
    elif not check_category_name(category):
        return False
    
    elif not due_date \
    or not due_date.replace('.', '').isdigit() \
    or len(due_date.split('.')) != 3:
        return False
    
    elif user_date <= current_date:
        print(f'Дата {due_date} меньше текущей {current_date}.')
        return False
    
    elif priority.lower() not in ['низкий', 'средний', 'высокий']:
        return False
    
    else:
        return True

def check_update_task(field: str, value: str) -> bool:
    '''Проверить корректность ввода полей для редактирования.'''
    
    fields = ['title', 'description', 'category', 'priority']
    categories = ['Личное', 'Обучение', 'Работа']
    priorities = ['Низкий', 'Средний', 'Высокий']
    if field.lower() not in fields:
        return False

    if field.lower() == "category" and value.capitalize() not in categories:
        return False

    if field.lower() == "priority" and value.capitalize() not in priorities:
        return False

    if field.lower() == "title" and not value.strip():
        return False
    
    return True
    
def check_status_task(status: str) -> bool:
    '''Проверить корректность ввода статуса задачи.'''
    
    statuses = ['Выполнена', 'Не выполнена']
    if status.capitalize() in statuses:
        return True
    else:
        return False