import sys
import os

# Добавляем корневую директорию в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic.crud import TaskFunctions as tf
from logic.validators import check_category_name, check_task, check_status_task


def main():
    '''Основное меню приложения.'''
    while True:
        print('\nМенеджер задач')
        print('1. Просмотреть все задачи')
        print('2. Посмотреть задачи по категории')
        print('3. Добавить задачу')
        print('4. Редактировать задачу')
        print('5. Отметить задачу выполненной')
        print('6. Удалить задачу')
        print('7. Искать задачу')
        print('0. Выйти')
        choice = input('Выберите действие: ')

        if choice == '1':
            tf.get_all_tasks()

        elif choice == '2':
            name = input('Введите название категории: ')
            if check_category_name(name):
                tf.get_tasks_by_category(name)
            else:
                print('Название категории введено некорректно.')

        elif choice == '3':

            title = input('Введите название задачи: ')
            description = input('Введите описание задачи: ')
            category = input('Введите название категории: ')
            due_date = input('Введите дату завершения задачи (Формат: dd.mm.yyyy): ')
            priority = input('Введите приоритет (низкий, средний, высокий): ')
            if check_task(title, category, due_date, priority):
                tf.create_task(title, description, category, due_date, priority)
            else:
                print('Введены некорректные данные.')

        elif choice == '4':
            task_id = int(input('Введите id задачи для редактирования: '))
            field = input(
                'Введите поле для редактирования (title, description, category, priority): '
            )
            value = input('Введите новое значение поля: ')
            tf.update_task(task_id, field, value)

        elif choice == '5':
            task_id = int(input('Введите id задачи для отметки выполненной: '))
            tf.complete_task(task_id)

        elif choice == '6':
            task_id = int(input('Введите id задачи для удаления: '))
            tf.delete_task(task_id)

        elif choice == '7':
            keyword = input('Введите ключевое слово для поиска: ')
            category = input(
                'Введите название категории (пустое поле для поиска по всем категориям): '
            )
            status = input('Введите статус выполненности (Выполнена/Не выполнена): ')
            if check_status_task(status):
                tf.search_task(keyword, category, status)

        elif choice == '0':
            break

        else:
            print('Некорректный ввод. Попробуйте снова.')


if __name__ == '__main__':
    main()
