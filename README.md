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
###### Примеры запросов находятся в файле Работа с БД.sql
###### Результаты запросов представлены на фото Запрос sql задание 1.png и Запрос sql задание 2.pngПредставь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
###### Примеры запросов находятся в файле Работа с БД.sql
###### Результаты запросов представлены на фото Запрос sql задание 1.png и Запрос sql задание 2.pngДля этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).

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
##### Примеры запросов находятся в файле Работа с БД.sql
##### Результаты запросов представлены на фото Запрос sql задание 1.png и Запрос sql задание 2.png
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

##### Результат запуска автотеста представлен на фото Запуск автотеста.png