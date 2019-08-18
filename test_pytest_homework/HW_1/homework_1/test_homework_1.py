import pytest

from homework_1.conftest import SimpleTypeDataClass


class TestSimpleTypeClass:
    """
    тесты для простых типов данных
    """

    @pytest.fixture(scope='function')
    def data_fixture(self):
        """
        тестируем создание фикстуры внутри класса поэтому не выносим ее в conftest.py
        fixture для создания тестовых данных для простых типов внутри класса
        :return:
        """
        test_data = SimpleTypeDataClass(2, 3, 'qwerty')
        return test_data

    def test_sum(self, data_fixture):
        """
        тест на сумму простых чисел
        :param data_fixture:
        :return:
        """
        assert data_fixture.a + data_fixture.b == 5

    def test_string_length(self, data_fixture):
        """
        тест на длинну строки
        :param data_fixture:
        :return:
        """
        string = data_fixture.some_string
        assert len(string) < 25

    def test_ass(self, data_fixture):
        """
        тест на сравнение суммы
        :param data_fixture:
        :return:
        """
        assert data_fixture.a + data_fixture.b < 10

    def test_char_list(self, data_fixture):
        """
        тест на данные в списке
        :param data_fixture:
        :return:
        """
        string = data_fixture.some_string
        char_list = list(string)
        assert char_list[2] == 'e'


class TestDataStructureClass:
    """
    тесты для data structures
    """

    def test_dict(self, data_structures_fixture):
        """
        проверка значения в словаре по ключу
        :param data_structures_fixture:
        :return:
        """
        my_dict = data_structures_fixture.my_dict
        assert my_dict['second'] == 2

    def test_tuple(self, data_structures_fixture):
        """
        проверка сравнения значения по номеру
        :param data_structures_fixture:
        :return:
        """
        my_tuple = data_structures_fixture.my_tuple
        assert my_tuple[3] == 4

    def test_set(self, data_structures_fixture):
        """
        сравнение рассматриваемого множества с указанным
        :param data_structures_fixture:
        :return:
        """
        my_set = data_structures_fixture.my_set
        assert my_set.issuperset({2, 3}) == True


def test_set(set_data_fixture):
    """
    тестирования сравнение set
    :param set_data_fixture:
    :return:
    """
    set_a = set_data_fixture
    set_b = {3, 2, 3, 1}
    assert set_a == set_b


def test_set_sum(set_data_fixture):
    """
    проверка суммы набора
    :param set_data_fixture:
    :return:
    """
    assert sum(set_data_fixture) == 6


def test_set_ass(set_data_fixture):
    """
    проверка минимального значения в наборе
    :param set_data_fixture:
    :return:
    """
    assert min(set_data_fixture) == 1
