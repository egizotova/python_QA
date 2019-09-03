import pytest


@pytest.fixture()
def breweries_name_fixture():
    """
    возвращает Filter breweries by name
    :return:
    """
    return 'https://api.openbrewerydb.org/breweries?by_name=cooper'


@pytest.fixture()
def query_string():
    return 'dog'


@pytest.fixture()
def аutocomplete_url_fixture(query_string):
    """
    возвращает урл
    :param search_string:
    :param autocomplete_url_fixture:
    :return:
    """

    autocomplete_url = ('https://api.openbrewerydb.org/breweries/autocomplete?query=' + query_string)
    return autocomplete_url

# https://api.openbrewerydb.org/breweries/autocomplete?query=dog
