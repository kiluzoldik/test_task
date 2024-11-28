import sys
import os

# Добавляем корневую директорию в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from repositories.schemas import BaseTask
from dataclasses import asdict


def to_dict(task: BaseTask) -> dict:
    '''Сериализовать объект Task в словарь.'''
    return asdict(task)

def from_input_to_object_task(
    task_id: int,
    title: str,
    description: str,
    category: str,
    due_date: str,
    priority: str,
) -> BaseTask:
    
    '''Создать объект Task из входных параметров.'''
    
    return BaseTask(
        task_id=task_id,
        title=title,
        description=description,
        category=category,
        due_date=due_date,
        priority=priority,
    )