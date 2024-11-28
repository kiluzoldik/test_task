import os
import json
from .validators import to_dict, from_input_to_object_task


lst_for_tasks = []

class TaskFunctions:
    
    '''Класс для работы с задачами.'''
    
    def get_all_tasks() -> list:
        '''Получить все задачи.'''
        if os.path.exists('tasks.json') and os.stat('tasks.json').st_size > 0:
            with open('tasks.json', 'r') as file:
                print(json.load(file))
            
        else:
            print('Файл tasks.json не найден.')
    
    def get_tasks_by_category(category_name: str) -> list:
        '''Получить все задачи по категории.'''
        if os.path.exists('tasks.json') and os.stat('tasks.json').st_size > 0:
            with open('tasks.json', 'r') as file:
                lst_for_tasks = json.load(file)
            
            print([task for task in lst_for_tasks if task.get('category') == category_name])
            
        else:
            print('Файл tasks.json не найден.')
    
    def create_task(*args):
        '''Создать новую задачу.'''
        if os.path.exists('tasks.json') and os.stat('tasks.json').st_size > 0: # Проверяем наличие и пустоту файла tasks.json
            with open('tasks.json', 'r') as file:
                
                try:
                    lst_for_tasks = json.load(file) # Загружаем существующие данные из файла
                    
                except json.JSONDecodeError:
                    print('Файл tasks.json поврежден, он будет перезаписан.')

        else:
            lst_for_tasks = []
                    
        task_id = max((task.get('task_id', 0) for task in lst_for_tasks), default=0) + 1 # Получаем максимальный task_id
        task = from_input_to_object_task(task_id, *args)
        
        try:
            lst_for_tasks.append(to_dict(task))
            
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump(lst_for_tasks, file, indent=2, ensure_ascii=False)
                
        except Exception as e:
            print(f'Ошибка при создании задачи: {e}')
        
        print('Задача успешно добавлена.')
        
    def update_task(task_id: int, field: str, value: str):
        '''Обновить существующую задачу.'''
        if os.path.exists('tasks.json') and os.stat('tasks.json').st_size > 0:
            try:
                with open('tasks.json', 'r') as file:
                    lst_for_tasks = json.load(file)
                
                for task in lst_for_tasks:
                    if task.get('task_id') == task_id:
                        if field in task.keys():
                            task[field] = value
                            with open('tasks.json', 'w', encoding='utf-8') as file:
                                json.dump(lst_for_tasks, file, indent=2, ensure_ascii=False)
                                
                                return 'Задача успешно изменена.'
                                
                        else:
                            return f'Поле "{field}" не существует в задаче.'
                    
                    print('Задача не найдена.')
                
            except Exception as e:
                print(f'Ошибка при редактировании задачи: {e}')
        
        else:
            print('Файл tasks.json не найден. Пожалуйста, добавьте хотя бы одну задачу.')
        
    def delete_task(task_id: int):
        '''Удалить существующую задачу.'''
        if os.path.exists('tasks.json') and os.stat('tasks.json').st_size > 0:
            try:
                with open('tasks.json', 'r') as file:
                    lst_for_tasks = json.load(file)
                
                for task in lst_for_tasks:
                    if task.get('task_id') == task_id:
                        lst_for_tasks.remove(task)
                        with open('tasks.json', 'w', encoding='utf-8') as file:
                            json.dump(lst_for_tasks, file, indent=2, ensure_ascii=False)
                            
                            print('Задача успешно удалена.')
                        
            except Exception as e:
                print(f'Ошибка при удалении задачи: {e}')
            
        else:
            print('Файл tasks.json не найден. Пожалуйста, добавьте хотя бы одну задачу.')
        
    def search_task(keyword: str, category: str, status: str):
        '''Поиск задач.'''
        if os.path.exists('tasks.json') and os.stat('tasks.json').st_size > 0:
            try:
                with open('tasks.json', 'r') as file:
                    lst_for_tasks = json.load(file)
                
                filtered_tasks = [task for task in lst_for_tasks if 
                                (keyword.lower in str(task.get('title', '')).lower or 
                                 keyword.lower in str(task.get('description', '')).lower) and
                                (category.lower == str(task.get('category', '')).lower or category.lower == '') and
                                (status.lower == str(task.get('status', '')).lower or status.lower == '')]
                
                if filtered_tasks:
                    for task in filtered_tasks:
                        print(task)
                        
                else:
                    print('Задачи не найдены.')
                    
            except Exception as e:
                print(f'Ошибка при поиске задач: {e}')
            
        else:
            print('Файл tasks.json не найден. Пожалуйста, добавьте хотя бы одну задачу.')
    