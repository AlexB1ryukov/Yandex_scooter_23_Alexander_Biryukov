from http.client import responses

import configuration
import requests
import data

#Создание заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)


#Получение данных о заказе по трек номеру
def get_data_order_with_track(track_number):
    url_get_order = f"{configuration.URL_SERVICE}{configuration.GET_ORDER}{track_number}"
    return requests.get(url_get_order)

#Авто тест для проверки того, что заказ создается и по полученному трек номеру можно получить данные о заказе
def test_order_created_and_data_is_being_output():
    order = create_order(data.order_body)

    #Получение трек номера созданного заказа
    track_number = order.json()["track"]
    print(f" Номер вашего заказа: {track_number}")
    #Получение данных заказа по треку
    response = get_data_order_with_track(track_number)
    assert response.status_code == 200, f"Запрос не прошел, ошибка: {response.status_code}"
    order_data = response.json()
    print(f"Данные вашего заказа: {order_data}")

# Александр Бирюков, 23-я когорта — Финальный проект. Инженер по тестированию плюс