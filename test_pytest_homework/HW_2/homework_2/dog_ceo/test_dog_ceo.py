"""
dog.ceo service test
"""
import pytest
import requests


@pytest.mark.parametrize("api_url", ['https://dog.ceo/api/breeds/list/all'])
def test_breed_list_success_response(api_url):
    """
    тест проверяет что сервис жив и возвразащает 200 HTTP status
    :param breed_url_fixture:
    :return:
    """
    response = requests.get(api_url)
    assert response.status_code == 200


@pytest.mark.parametrize("breed_wrong_url",
                         ['https://dog.ceo/api/breeds/list/dogs',
                          'https://dog.ceo/api/breeds/list/cats'])
def test_breed_list_not_found_response(breed_wrong_url):
    """
    тест проверяет что сервис на несуществующие url возвразащает 404 HTTP status
    использует параметризацию для 2х невепных url
    :param breed_wrong_url:
    :return:
    """
    response = requests.get(breed_wrong_url)
    assert response.status_code == 404


def test_breed_list_has_breeds(breed_url_fixture):
    """
    тест проверяет что список пород не пустой
    :param breed_url_fixture:
    :return:
    """
    response = requests.get(breed_url_fixture)
    response_json = response.json()
    messages = response_json['message']
    if messages:
        messages_count = len(messages)
    assert messages_count > 0


def test_random_dog(random_dog_url_fixture):
    """
    тест проверяет что api для получения картинки со
    случайной собаки отвечает co статусом success
    :param random_dog_url_fixture:
    :return:
    """
    response = requests.get(random_dog_url_fixture)
    response_json = response.json()
    assert response_json['status'] == 'success'


def test_random_dog_image(breed_images_url_fixture):
    """
    тест проверяет что api для получения списка изображений возвращает не пустой результат
    :param breed_images_url_fixture:
    :return:
    """
    breed_images_response = requests.get(breed_images_url_fixture)
    messages = breed_images_response.json()['message']
    if messages:
        messages_count = len(messages)
    assert messages_count > 0
