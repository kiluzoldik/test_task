from logic.crud import TaskManagerFunctions as tmf
from logic.crud import TaskFunctions as tf


def main():
    while True:
        print('\nМенеджер задач')
        print('1. Просмотреть все задачи')
        print('2. Добавить категорию')
        print('3. Добавить задачу')
        print('4. Редактировать задачу')
        print('5. Отметить задачу выполненной')
        print('6. Удалить задачу')
        print('7. Искать задачу')
        print('0. Выйти')
        choice = input('Выберите действие: ')
        
        if choice == '1':
            tmf.get_tasks()
        
        elif choice == '2':
            name = input('Введите название категории: ')
            tmf.create_category(name)
        
        elif choice == '3':
            title = input('Введите название задачи: ')
            description = input('Введите описание задачи: ')
            category = input('Введите название категории: ')
            due_date = input('Введите дату и время выполнения: ')
            priority = int(input('Введите приоритет (от 1 до 10): '))
            tmf.create_task(title, description, category, due_date, priority)
            
        elif choice == '4':
            task_id = int(input('Введите id задачи для редактирования: '))
            field = input('Введите поле для редактирования (title, description, category, completed): ')
            value = input('Введите новое значение поля: ')
            tf.update_task(task_id, **{field: value})
            
        elif choice == '5':
            task_id = int(input('Введите id задачи для отметки выполненной: '))
            tf.update_task(task_id, completed=True)
            
        elif choice == '6':
            task_id = int(input('Введите id задачи для удаления: '))
            tf.delete_task(task_id)
            
        elif choice == '7':
            keyword = input('Введите ключевое слово для поиска: ')
            category = input('Введите название категории (пустое поле для поиска по всем категориям): ')
            completed = input('Введите статус выполненности (True/False): ')
            tf.search_task(keyword, category, completed)
            
        elif choice == '0':
            break
        
        else:
            print('Некорректный ввод. Попробуйте снова.')
            

if __name__ == '__main__':
    main()
            