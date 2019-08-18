import pytest
import requests
import sys
import argparse

#
# print(sys.argv)
#
# args = sys.argv
# def calculate(num1, num2):
#     return int(num1) + int(num2)
#
# print(calculate(args[1], args[2]))

parser =argparse.ArgumentParser()

parser.add_argument('--metod', '-m'
                    action = 'store',
                    help = 'Method to make request'
                    default = 'GET')

# Написать минимум 5 тестов для REST API сервиса: https://dog.ceo/dog-api/.
# Как минимум 2 из 5 должны использовать параметризацию.
# Документация к API есть на сайте.
# Тесты должны успешно проходить.
# тесты для сервиса dog.ceo
class TestDocCeoClass:

    # fixture врозвращает url для списка пород
    @pytest.fixture()
    def breed_url_fixture(self):
        return 'https://dog.ceo/api/breeds/list/all'

    # fixture врозвращает неверный url для списка пород
    @pytest.fixture()
    def breed_wrong_url_fixture(self):
        return 'https://dog.ceo/api/breeds/list/dogs'

    # fixture врозвращает url для api случайной картинки собаки
    @pytest.fixture()
    def random_dog_url_fixture(self):
        return 'https://dog.ceo/api/breeds/image/random'

    # fixture врозвращает url для списка изображения породы
    @pytest.fixture()
    def breed_images_url_fixture(self, breed_url_fixture):
        response = requests.get(breed_url_fixture)
        response_json = response.json()
        breed_name_dict = response_json['message']
        breed_name = list(breed_name_dict.keys())[0]
        breed_images_url = 'https://dog.ceo/api/breed/{0}/images'.replace('{0}', breed_name)
        return breed_images_url

    # тест проверяет что сервис жив и возвразащает 200 HTTP status
    def test_breed_list_success_response(self, breed_url_fixture):
        response = requests.get(breed_url_fixture)
        assert response.status_code == 200
        # тест проверяет что сервис жив и возвразащает 200 HTTP status

    # тест проверяет что сервис на несуществующий url возвразащает 404 HTTP status
    def test_breed_list_not_found_response(self, breed_wrong_url_fixture):
        response = requests.get(breed_wrong_url_fixture)
        assert response.status_code == 404

    # тест проверяет что список пород не пустой
    def test_breed_list_has_breeds(self, breed_url_fixture):
        response = requests.get(breed_url_fixture)
        response_json = response.json()
        assert len(response_json['message']) > 0

    # тест проверяет что api для получения картинки со случайной собаки отвечает co статусом success
    def test_random_dog(self, random_dog_url_fixture):
        response = requests.get(random_dog_url_fixture)
        response_json = response.json()
        assert response_json['status'] == 'success'

    # тест проверяет что api для получения списка изображений возвращает не пустой результат
    def test_random_dog(self, breed_images_url_fixture):
        breed_images_response = requests.get(breed_images_url_fixture)
        assert len(breed_images_response.json()['message']) > 0

#
#
# 1. Тестирование REST сервиса 1
# Написать минимум 5 тестов для REST API сервиса: https://dog.ceo/dog-api/.
# Как минимум 2 из 5 должны использовать параметризацию.
# Документация к API есть на сайте.
# Тесты должны успешно проходить.
#
# 2. Тестирование REST сервиса 2
# Написать минимум 5 тестов для REST API сервиса: https://www.openbrewerydb.org/.
# Как минимум 2 из 5 должны использовать параметризацию.
# Документация к API есть на сайте.
# Тесты должны успешно проходить.
#
# 3. Тестирование REST сервиса 3.
# Написать минимум 5 тестов для REST API сервиса: https://jsonplaceholder.typicode.com/.
# Как минимум 2 из 5 должны использовать параметризацию.
# Документация к API есть на сайте.
# Тесты должны успешно проходить.
#
# 4. Реализуйте в отдельном модуле (файле) тестовую функцию, которая будет проверять ответ переданного через парамтер url на 200.
# У параметра url должно быть значение по умолчанию https://ya.ru (будем надеяться яндекс выдержит!)
# Параметр должен быть реализован через pytest.addoption
# Критерии оценки: Наличие скриншота выполнения тестов с флагом -v
# Желательно не просто проверять ответы 200 по урлам, а получать данные и проверять что-то в них.
# Код должен быть проверен и преведе в соотвествие с рекомендациями pylint.
# В качестве результата домашнего задания необходимо прислать ссылку на коммит в вашем github репозитории и вывод работы pylint.
