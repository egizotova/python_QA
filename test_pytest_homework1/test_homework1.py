import pytest


# данные для тестирования простых типов
class SimpleTypeDataClass:

    def __init__(self, a: int, b: int, some_string: str):
        self.a = a
        self.b = b
        self.some_string = some_string


# тесты для простых типов данных
class TestSimpleTypeClass:

    # fixture для создания тестовых данных для простых типов внутри класса
    @pytest.fixture(scope='function')
    def data_fixture(self):
        test_data = SimpleTypeDataClass(2, 3, 'qwerty')
        return test_data

    # тест на сумму простых чисел
    def test_sum(self, data_fixture):
        assert data_fixture.a + data_fixture.b == 5

    # тест на длинну строки
    def test_string_length(self, data_fixture):
        string = data_fixture.some_string
        assert len(string) < 25

    # тест на данные в списке
    def test_char_list(self, data_fixture):
        string = data_fixture.some_string
        char_list = list(string)
        assert char_list[2] == 'e'


# данные для тестирования спиcков, словарей и объединений
class StructureDataClass:

    def __init__(self, my_set: set, my_tuple: tuple, my_dict: dict):
        self.my_set = my_set
        self.my_tuple = my_tuple
        self.my_dict = my_dict


# fixture для теста yield
@pytest.fixture(scope='session')
def session_fixture():
    print('\nsession fixture started')
    yield
    print('\nsession fixture completed')


# fixture для создания тестовых данных для data structures и передачи другой fixture в качестве параметра
@pytest.fixture(scope='session')
def data_structures_fixture(session_fixture):
    my_tuple1 = (1, 2, 3, 4, 5)
    my_dict1 = {
        'first': 1,
        'second': 2,
        'third': 3
    }
    my_set1 = {1, 2, 3}
    test_data = StructureDataClass(my_set1, my_tuple1, my_dict1)
    return test_data


# тесты для data structures
class TestDataStructureClass:

    def test_dict(self, data_structures_fixture):
        my_dict = data_structures_fixture.my_dict
        assert my_dict['second'] == 2

    def test_tuple(self, data_structures_fixture):
        my_tuple = data_structures_fixture.my_tuple
        assert my_tuple[3] == 4

    def test_set(self, data_structures_fixture):
        my_set = data_structures_fixture.my_set
        assert my_set.issuperset({2, 3}) == True


# fixture для создания тестовых данных для set
@pytest.fixture(scope='module')
def set_data_fixture():
    my_set = {1, 2, 3}
    return my_set


# тестирования set
def test_set(set_data_fixture):
    set_a = set_data_fixture
    set_b = {3, 2, 3, 1}
    assert set_a == set_b