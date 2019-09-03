"""
openbrewerydb.org service test
"""
import pytest
import requests


@pytest.mark.parametrize("api_url", ['https://api.openbrewerydb.org/breweries'])
def test_of_brewerys(api_url):
    """
    список не пустой
    :param api_url:
    :return:
    """
    response = requests.get(api_url)
    response_json = response.json()

    assert len(response_json) > 0


@pytest.mark.parametrize("api_url", ['https://api.openbrewerydb.org/breweries'])
def test_list_name(api_url):
    """
    проверяем, что в списке есть указанная страна
    :param api_url:
    :return:\'p0=
    """
    response = requests.get(api_url)
    response_json = response.json()
    has_country = False
    for brewery in response_json:
        if brewery['country'] == 'United States':
            has_country = True

    assert has_country


def test_filter_name(breweries_name_fixture):
    """
    проверяет что в ответе все элементы соодержат элемент фильтра
    :param breweries_name_fixture:
    :return:
    """
    response = requests.get(breweries_name_fixture)
    response_json = response.json()
    has_name = True
    for brewery in response_json:
        name_lower_case = str(brewery['name']).lower()
        if 'cooper' not in name_lower_case:
            has_name = False
    assert has_name


@pytest.mark.parametrize("api_url", ['https://api.openbrewerydb.org/breweries?page=2&per_page=20'])
def test_pangination(api_url):
    """
    проверка пангинации
    :param api_url:
    :return:
    """
    response = requests.get(api_url)
    response_json = response.json()

    assert len(response_json) == 20


# @pytest.mark.parametrize("аutocomplete_url_fixture", ['dog'])
def test_autocomplete(аutocomplete_url_fixture):
    """
    проверка, что в ответе нет элементов несодержащих искомое
    :param аutocomplete_url_fixture:
    :return:
    """
    response = requests.get(аutocomplete_url_fixture)
    response_json = response.json()
    has_autocomplete = True
    for brewery in response_json:
        name_lower_case = str(brewery['name']).lower()
        if 'dog' not in name_lower_case:
            has_autocomplete = False
    assert has_autocomplete
