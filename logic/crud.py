import os
import json

from .validators import to_dict, from_input_to_object_task
from exceptions.exceptions import (
    FileNotFoundError, 
    TaskNotFoundError, 
    FieldNotFoundError, 
    InvalidFileError,
    CreateTaskError,
    UpdateTaskError,
    DeleteTaskError,
    SearchTaskError)


lst_for_tasks = []


class TaskFunctions:
    '''Класс для работы с задачами.'''

    def get_all_tasks() -> list:
        '''Получить все задачи.'''
        if os.path.exists('tasks.json') and os.stat('tasks.json').st_size > 0:
            with open('tasks.json', 'r') as file:
                print(json.dumps(json.load(file), indent=2, ensure_ascii=False))
        else:
            raise FileNotFoundError()

    def get_tasks_by_category(category_name: str) -> list:
        '''Получить все задачи по категории.'''
        if os.path.exists('tasks.json') and os.stat('tasks.json').st_size > 0:
            with open('tasks.json', 'r') as file:
                lst_for_tasks = json.load(file)

                [
                    print(json.dumps(task, indent=2, ensure_ascii=False))
                    for task in lst_for_tasks
                    if task.get('category') == category_name
                ]
        else:
            raise FileNotFoundError()

    def create_task(*args):
        '''Создать новую задачу.'''
        if (
            os.path.exists('tasks.json') and os.stat('tasks.json').st_size > 0
        ):  # Проверяем наличие и пустоту файла tasks.json
            with open('tasks.json', 'r') as file:
                try:
                    lst_for_tasks = json.load(
                        file
                    )  # Загружаем существующие данные из файла

                except InvalidFileError as e:
                    print(f'{e}, он будет перезаписан.')

        else:
            lst_for_tasks = []

        task_id = (
            max((task.get('task_id', 0) for task in lst_for_tasks), default=0) + 1
        )  # Получаем максимальный task_id
        task = from_input_to_object_task(task_id, *args)
        try:
            lst_for_tasks.append(to_dict(task))
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump(lst_for_tasks, file, indent=2, ensure_ascii=False)
                return print('Задача успешно добавлена.')

        except CreateTaskError as e:
            print(e)

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
                                json.dump(
                                    lst_for_tasks, file, indent=2, ensure_ascii=False
                                )
                                return print('Задача успешно изменена.')
                        else:
                            print(FieldNotFoundError(field))
                            
                return print(TaskNotFoundError(task_id))

            except UpdateTaskError as e:
                print(e)

        else:
            print(FileNotFoundError())
        
    def complete_task(task_id: int):
        '''Завершить существующую задачу.'''
        if os.path.exists('tasks.json') and os.stat('tasks.json').st_size > 0:
            try:
                with open('tasks.json', 'r') as file:
                    lst_for_tasks = json.load(file)

                for task in lst_for_tasks:
                    if task.get('task_id') == task_id:
                        task['status'] = 'Выполнена'
                        with open('tasks.json', 'w', encoding='utf-8') as file:
                            json.dump(lst_for_tasks, file, indent=2, ensure_ascii=False)
                            print('Задача успешно завершена.')

            except:
                return SearchTaskError(message='Не удалось найти задачу.')
        else:
            print(FileNotFoundError())

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
                            return print('Задача успешно удалена.')
                            
                return print(TaskNotFoundError(task_id))

            except DeleteTaskError as e:
                print(e)

        else:
            print(FileNotFoundError())

    def search_task(keyword: str, category: str, status: str):
        '''Поиск задач.'''
        if os.path.exists('tasks.json') and os.stat('tasks.json').st_size > 0:
            try:
                with open('tasks.json', 'r') as file:
                    lst_for_tasks = json.load(file)

                filtered_tasks = [
                    task
                    for task in lst_for_tasks
                    if (
                        keyword.capitalize() in str(task.get('title', ''))
                        or keyword.capitalize() in str(task.get('description', ''))
                    )
                    and (
                        category.capitalize() == str(task.get('category', ''))
                        or category.capitalize() == ''
                    )
                    and (
                        status.capitalize() == str(task.get('status', ''))
                        or status.capitalize() == ''
                    )
                ]

                if filtered_tasks:
                    for task in filtered_tasks:
                        print(task)

                else:
                    return print(SearchTaskError())

            except:
                raise SearchTaskError('Ошибка при поиске задач.')

        else:
            print(FileNotFoundError())
