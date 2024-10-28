﻿# Дипломный проект на курс "Инженер по тестированию расширенный"

## Описание проекта:

## Первая практическая часть
### 1. Тестирование функциональности веб-приложения Яндекс самокат
### 2. Ретест багов в мобильном приложении Яндекс самокат
### 3. Регрессионное тестирование мобильного приложения по готовым тест-кейсам
Вся тестовая документация будет приложена в репозиторий
## Вторая практическая часть
### 1. Работа с базой данных
#### Задание 1
###### Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
###### Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).
###### Примеры запросов находятся в файле Работа с БД.sql
###### Результаты запросов представлены на фото Запрос sql задание 1.png и Запрос sql задание 2.png
##### Задание 2
###### Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
###### Для этого: выведи все трекеры заказов и их статусы. 
###### Статусы определяются по следующему правилу:
###### Если поле finished == true, то вывести статус 2.
###### Если поле canсelled == true, то вывести статус -1.
###### Если поле inDelivery == true, то вывести статус 1.
###### Для остальных случаев вывести 0.
###### Технические примечания:
###### Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent. Пароль: smith.
###### У psql есть особенность: если таблица в базе данных с большой буквы, то её в запросе нужно брать в кавычки. Например, select * from “Orders”.
##### Примеры запросов находятся в файле [Работа с БД.sql](https://github.com/AlexB1ryukov/Yandex_scooter_23_Alexander_Biryukov/blob/9ec60cbe0ed649125b74ae5e7d98e0b81fc3fd0e/%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%D1%81%20%D0%91%D0%94.sql)
##### Результаты запросов представлены на фото [Запрос sql задание 1.png](https://github.com/AlexB1ryukov/Yandex_scooter_23_Alexander_Biryukov/blob/3f28ef0f6322a6b9660ca8fde8af0b2aa2788ff9/%D0%97%D0%B0%D0%BF%D1%80%D0%BE%D1%81%20sql%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%201.png) и [Запрос sql задание 2.png](https://github.com/AlexB1ryukov/Yandex_scooter_23_Alexander_Biryukov/blob/9ec60cbe0ed649125b74ae5e7d98e0b81fc3fd0e/%D0%97%D0%B0%D0%BF%D1%80%D0%BE%D1%81%20sql%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%202.png)
### 2. Автоматизация теста к API
#### Cценарий для автоматизации:
1) Клиент создает заказ.
2) Проверяется, что по треку заказа можно получить данные о заказе.
#### Шаги автотеста:
1) Выполнить запрос на создание заказа.
2) Сохранить номер трека заказа.
3) Выполнить запрос на получения заказа по треку заказа.
4) Проверить, что код ответа равен 200.

###### Для запуска теста необходимо в файл configuration скопировать рабочий URL стенда
###### Для тестирование необходимо загрузить библиотеки requests и pytest

##### Результат запуска автотеста представлен на фото [Запуск автотеста.png](https://github.com/AlexB1ryukov/Yandex_scooter_23_Alexander_Biryukov/blob/4f7d8eec751a170b5c8730bd0f7c6bf792eba9b1/%D0%97%D0%B0%D0%BF%D1%83%D1%81%D0%BA%20%D0%B0%D0%B2%D1%82%D0%BE%D1%82%D0%B5%D1%81%D1%82%D0%B0.png)
