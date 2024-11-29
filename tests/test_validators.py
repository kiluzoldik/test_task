import pytest

from logic.validators import check_category_name, check_task, check_update_task, check_status_task


class TestValidatorsFunctions:
    
    @pytest.mark.parametrize(
        "category_name, expected_result",
        [
            ("Личное", True),
            ("Обучение", True),
            ("Работа", True),
            ("Новая категория", False),
            ("work", False),
            ("personal", False),
        ]
    )
    def test_check_category_name(self, category_name, expected_result):
        """Тест на корректность категорий."""
        assert check_category_name(category_name) == expected_result
        
    @pytest.mark.parametrize(
        "title, category, due_date, priority, expected_result",
        [
            ("Задача 1", "Личное", "01.01.2025", "Низкий", True),
            ("Задача 2", "Работа", "01.01.2025", "Средний", True),
            ("Задача 3", "Обучение", "01.01.2025", "Высокий", True),
            ("", "Личное", "01.01.2025", "Низкий", False),
            ("Задача", "", "01.01.2025", "Низкий", False),
            ("Задача", "Новая категория", "01.01.2025", "Низкий", False),
            ("Задача", "Личное", "32.13.2025", "Низкий", False),
            ("Задача", "Личное", "01.01.2020", "Низкий", False),
            ("Задача", "Работа", "01.01.2025", "Очень высокий", False),
        ]
    )
    def test_check_task(self, title, category, due_date, priority, expected_result):
        """Тест на корректность ввода задачи."""
        assert check_task(title, category, due_date, priority) == expected_result
        
    @pytest.mark.parametrize(
        "field, value, expected_result",
        [
            ("title", "New Title", True),
            ("category", "Работа", True),
            ("priority", "Средний", True),
            ("description", "Some description", True),
            ("unknown_field", "Some value", False),
            ("category", "Новая категория", False),
            ("priority", "Очень высокий", False),
            ("title", "", False),
        ]
    )
    def test_check_update_task(self, field, value, expected_result):
        """Тест на корректность ввода полей для редактирования."""
        assert check_update_task(field, value) == expected_result
        
    @pytest.mark.parametrize(
        "status, expected_result",
        [
            ("Выполнена", True),
            ("Не выполнена", True),
            ("Завершена", False),
            ("Не завершена", False),
            ("Completed", False),
        ]
    )
    def test_check_status_task(self, status, expected_result):
        """Тест на корректность ввода статуса задачи."""
        assert check_status_task(status) == expected_result