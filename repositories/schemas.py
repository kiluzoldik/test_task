from dataclasses import dataclass


@dataclass
class BaseTask:
    task_id: int
    title: str
    description: str
    category: str
    due_date: str
    priority: str
    status: str = 'Не выполнена'
    