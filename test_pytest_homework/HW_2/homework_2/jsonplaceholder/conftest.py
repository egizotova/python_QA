import pytest


@pytest.fixture()
def base_url_fixture():
    """
    :return:
    """
    return 'https://jsonplaceholder.typicode.com/posts'


def pytest_addoption(parser):
    """
    parser.addoption
    :param :
    :return:
    """
    parser.addoption("--query", action="store", default="cat", help="query string")


@pytest.fixture()
def query_fixture(request):
    """
    :param request:
    :return:
    """
    query = request.config.getoption("--query")
    autocomplete_url = ('https://jsonplaceholder.typicode.com' + query)
    return autocomplete_url
