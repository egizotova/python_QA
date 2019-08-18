import pytest


class SimpleTypeDataClass:
    """
    данные для тестирования простых типов
    """

    def __init__(self, a: int, b: int, some_string: str):
        self.a = a
        self.b = b
        self.some_string = some_string


@pytest.fixture(scope='session')
def session_fixture():
    """
    fixture для теста yield
    :return:
    """
    print('\nsession fixture started')
    yield
    print('\nsession fixture completed')


class StructureDataClass:
    """
    данные для тестирования спиcков, словарей и объединений
    """

    def __init__(self, my_set: set, my_tuple: tuple, my_dict: dict):
        self.my_set = my_set
        self.my_tuple = my_tuple
        self.my_dict = my_dict


@pytest.fixture(scope='session')
def data_structures_fixture(session_fixture):
    """
    fixture для создания тестовых данных для data structures и передачи другой fixture в качестве параметра
    :param session_fixture:
    :return:
    """
    my_tuple1 = (1, 2, 3, 4, 5)
    my_dict1 = {
        'first': 1,
        'second': 2,
        'third': 3
    }
    my_set1 = {1, 2, 3}
    test_data = StructureDataClass(my_set1, my_tuple1, my_dict1)
    return test_data


@pytest.fixture(scope='module')
def set_data_fixture():
    """
    fixture для создания тестовых данных для set
    :return:
    """
    my_set = {1, 2, 3}
    return my_set
