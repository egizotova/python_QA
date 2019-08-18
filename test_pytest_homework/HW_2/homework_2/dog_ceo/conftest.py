"""
dog.ceo service test configuration
"""
import pytest
import requests


@pytest.fixture()
def breed_url_fixture():
    """
    fixture врозвращает url для списка пород
    :return: breed url
    """
    return 'https://dog.ceo/api/breeds/list/all'


@pytest.fixture()
def random_dog_url_fixture():
    """
    fixture возвращает url для api случайной картинки собаки
    :return: random image url
    """
    return 'https://dog.ceo/api/breeds/image/random'


@pytest.fixture()
def breed_images_url_fixture(breed_url_fixture):
    """
    fixture врозвращает url для списка изображения породы
    :param breed_url_fixture:
    :return: breed list url
    """
    response = requests.get(breed_url_fixture)
    response_json = response.json()
    breed_name_dict = response_json['message']
    breed_name = list(breed_name_dict.keys())[0]
    breed_images_url = 'https://dog.ceo/api/breed/{0}/images'.replace('{0}', breed_name)
    return breed_images_url
