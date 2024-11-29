class TaskError(Exception):
    '''Базовое исключение для ошибок задач.'''
    pass


class FileNotFoundError(TaskError):
    '''Исключение, если файл tasks.json не найден или пуст.'''
    def __init__(self, message='Файл tasks.json не найден или пуст.'):
        super().__init__(message)
        
        
class CreateTaskError(TaskError):
    '''Исключение, если не удалось создать новую задачу.'''
    def __init__(self, message='Не удалось создать новую задачу.'):
        super().__init__(message)
        
        
class UpdateTaskError(TaskError):
    '''Исключение, если не удалось изменить задачу.'''
    def __init__(self, message='Не удалось изменить задачу.'):
        super().__init__(message)
        
        
class DeleteTaskError(TaskError):
    '''Исключение, если не удалось удалить задачу.'''
    def __init__(self, message='Не удалось удалить задачу.'):
        super().__init__(message)
        
        
class SearchTaskError(TaskError):
    '''Исключение, если не удалось найти задачу.'''
    def __init__(self, message='Не удалось найти задачи.'):
        super().__init__(message)


class TaskNotFoundError(TaskError):
    '''Исключение, если задача с указанным ID не найдена.'''
    def __init__(self, task_id):
        message = f'Задача с ID {task_id} не найдена.'
        super().__init__(message)


class FieldNotFoundError(TaskError):
    '''Исключение, если указанное поле не найдено в задаче.'''
    def __init__(self, field):
        message = f'Поле "{field}" не существует в задаче.'
        super().__init__(message)


class InvalidFileError(TaskError):
    '''Исключение, если файл поврежден или содержит неверный формат данных.'''
    def __init__(self, message='Файл tasks.json поврежден'):
        super().__init__(message)
