from dataclasses import dataclass


@dataclass
class BaseTask:
    task_id: int
    title: str
    description: str
    category: str
    due_date: str
    priority: int
    completed: bool = False
    
@dataclass
class BaseCatetegory:
    catetegory_id: int
    name: str