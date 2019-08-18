"""
Реализуйте в отдельном модуле (файле) тестовую функцию,
которая будет проверять ответ переданного через парамтер url на 200.
У параметра url должно быть значение по умолчанию https://ya.ru
(будем надеяться яндекс выдержит!)
Параметр должен быть реализован через pytest.addoption
"""
import pytest


def pytest_addoption(parser):
    """
    parser.addoption
    :param parser:
    :return:
    """
    parser.addoption("--url", action="store", default="https://ya.ru", help="testing url")


@pytest.fixture
def param_url(request):
    """
    fixture return value of url passed in params
    :param request:
    :return:
    """
    return request.config.getoption("--url")
