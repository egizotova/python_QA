"""
jsonplaceholder service test
"""
import pytest
import requests


@pytest.mark.parametrize("api_url", ['https://jsonplaceholder.typicode.com'])
def test_placeholder(api_url):
    """
    проверяет что сервер присылает ответ 200
    :param api_url:
    :return:
    """
    response = requests.get(api_url)
    assert response.status_code == 200


def test_json_post_data(base_url_fixture):
    """
    проверка добавления
    :param base_url_fixture:
    :return:
    """
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': '1'
    }
    response = requests.post(url='https://jsonplaceholder.typicode.com/posts', data=data)
    print(response.json())
    assert response.status_code == 201


def test_query_params_search(query_fixture):
    """
/posts	100 posts
/comments	500 comments
/albums	100 albums
/photos	5000 photos
/todos	200 todos
/users	10 users

    :param query_fixture:
    :return:
    """
    response = requests.get(query_fixture)
    response_json = response.json()
    assert len(response_json) > 0


def test_email(query_fixture):
    """
    проверка что email не пустые
    :param query_fixture:
    :return:
    """
    response = requests.get(query_fixture)
    response_json = response.json()
    has_email = True
    for data in response_json:
        if len(data['email']) <= 0:
            has_email = False
    assert has_email
