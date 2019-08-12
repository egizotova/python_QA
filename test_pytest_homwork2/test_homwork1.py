import pytest

# 1. Написать не менее 10 базовых тестов на основные операции с базовыми типами данных
# (строки, числа, списки, словари, кортежи, множества) в Python, в качестве тестового фреймворка использовать pytest.
# 2. В тестах необходимо использовать все виды фикстур (session, module, function)
# 3. Должно быть выполнение каких-либо действий по завершению теста.
# 4. В docstring тестов должно присутствовать описание тестов.
# 5. Добавить инструкцию по запуску тестов на гитхаб.
# 6. Тесты должны успешно проходить стилистический анализ с помощью pylint.
# 7. В качестве решения приложить ссылку на коммит в гитхабе и результат выполнения тестов в виде скриншота.
# 8. Все тесты должны проходить успешно.

# @pytest.fixture(scope="function")
# def setup_function_fixture():
#     print("\nHello from setup function fixture!\n")
#     yield
#     print("\nBye bye from setup function fixture!\n")
#
#
# @pytest.fixture(scope="module")
# def setup_function_fixture():
#     print("\nHello from setup module fixture!\n")
#     yield
#     print("\nBye bye from setup module fixture!\n")


class TestClass():

    def _init_(self, a, b, name):
        self.a = a
        self.b = b
        self.name = eeeeeeee
        self.name = name
    def sum(self):
        return self.a + self.b


@pytest.fixture()
def _init_data_fixture():
    test_data = TestClass()
    return test_data



def test_sum(_init_data_fixture):
    assert _init_data_fixture.sum() == 5


# def test_string_length(init_data_fixture2):
#     string = init_data_fixture.name
#     assert len(string) < 25


def test_list(_init_data_fixture):
    string = _init_data_fixture.name
    char_list = list(string)
    print(char_list)
    assert char_list[2] == 'e'


def test_dict(_init_data_fixture):
    dict = {
        'first': 1,
        'second': 2,
        'third': 3
    }
    print(dict)
    assert dict['second'] == 2


def test_tuple(_init_data_fixture):
    my_tuple = (1, 2, 3, 4, 5)
    print(my_tuple)
    assert my_tuple[3] == 4


def test_set(_init_data_fixture):
    set_a = {1, 2, 3}
    set_b = {3, 2, 3, 1}

    assert set_a == set_b


def test_set(_init_data_fixture):
    set_a = {1, 2, 3}
    set_b = {3, 2, 3, 1}

    assert set_a == set_b



# class TestClass:
#
#     def test_two(self, init_data_fixture):
#         print("\nPrint from 'test_two'")
#
#     def test_three(self, init_data_fixture):
#         print("\nPrint from 'test_three'")