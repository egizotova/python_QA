"""
test service url
"""

import requests


def test_url(param_url):
    """
    test service by url passed in params
    :param param_url:
    :return:
    """
    response = requests.get(param_url)
    assert response.status_code == 200
    # если сервис ответил 200 то проверяем по заголовку json или html и далее сомтрим что не пустая страницы
    content_type = str(response.headers['Content-Type']).lower()
    if 'text/html' in content_type:
        assert 'body' in response.text.lower()
    elif 'application/json'.lower() in content_type:
        data = response.json()
        assert bool(data) is True
