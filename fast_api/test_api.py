import uvicorn
import pytest
import requests
from http import HTTPStatus
from fastapi import FastAPI
from lesson1.api_tests.case.data.case import *

url = 'http://127.0.0.1:8000/testcases/'
msg = "======wrong status code======"
# Создание экземпляра приложения FastAPI
app = FastAPI()


def create_new_tc():
    response = requests.post(url, json=create_case_dict)
    return response.json().get('id')


# if response.status_code == 200 else None

@pytest.mark.get
def test_get_data():
    resp = requests.get(url)
    assert resp.status_code == HTTPStatus.OK, msg


@pytest.mark.post
def test_post_t_case():
    response = requests.post(url, json=create_case_dict)
    print(response.text)
    assert response.status_code == HTTPStatus.OK, (f"===Неправильный код состояния====\nОжидалось: {HTTPStatus.OK},"
                                                   f"Получено: {response.status_code}\nОтвет: {response.text}")


@pytest.mark.get
def test_get_case_id():
    tc_id = create_new_tc()  # Создаем новый тестовый кейс и получаем его ID
    response = requests.get(url + f'{tc_id}')
    print(f'ID: {tc_id}')  # Для проверки
    data = response.json()
    assert data['id'] == tc_id
    request_info = (
        f"\n=== Запрос ===\n"
        f"URL: {url}\n"
        f"Метод: POST\n"
        f"Заголовки: {response.request.headers}\n"
        f"Тело запроса: {create_case_dict}\n"
    )

    response_info = (
        f"\n=== Ответ ===\n"
        f"Код состояния: {response.status_code}\n"
        f"Ожидалось: {HTTPStatus.OK}\n"
        f"Тело ответа: {response.text}\n"
        f"Заголовки ответа: {response.headers}\n"
    )

    assert response.status_code == HTTPStatus.OK, (
        f"=== Ошибка: Неправильный код состояния ===\n"
        f"{request_info}"
        f"{response_info}")


@pytest.mark.put
def test_update_tc():
    response = requests.put(url + f'{create_new_tc()}', json=case2)
    assert response.status_code == HTTPStatus.OK, msg


@pytest.mark.delete
def test_delete_tc():
    response = requests.delete(url + f'{create_new_tc()}')
    assert response.status_code == HTTPStatus.OK, msg


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
