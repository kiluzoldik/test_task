from repositories.schemas import BaseTask
import json


class CategoryFunctions:
    
    def create_category(self, name: str):
        ...
        
    def update_category(self, updated_name: str):
        ...
        
    def delete_category(self, name: str):
        ...
        
    def search_category(self, name: str):
        ...

class TaskFunctions:
    
    def create_task(
        self,
        title: str,
        description: str,
        category: str,
        due_date: str,
        priority: int,
    ):
        ...
        
    def update_task(
        self,
        task_id: int,
        title: str = None,
        description: str = None,
        category: str = None,
        completed: bool = False,
    ):
        ...
        
    def delete_task(self, title: str):
        ...
        
    def search_task(
        self, 
        keyword: str = None, 
        category: str = None, 
        completed: bool = False
    ):
        ...
    
class TaskManagerFunctions:
    
    def get_tasks(self):
        ...
