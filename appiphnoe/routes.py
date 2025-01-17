# -*- coding: utf-8 -*-
# Подключаем объект приложения Flask из __init__.py
from appiphnoe import app #,db
# Подключаем библиотеку для "рендеринга" html-шаблонов из папки templates
from flask import render_template, make_response, request, Response, jsonify, json, session, redirect, url_for
from . import dbservice
import functools



navmenu = [
    {
        'name': 'Главная',
        'addr': '/index'
    },
    {
        'name': 'Аккаунт',
        'addr': '/account'
    },
    {
        'name': 'Что нового',
        'addr': '/whatnew'
    },
    {
        'name': 'Цвет',
        'addr': '/color'
    },
    {
        'name': 'Заказ',
        'addr': '/order'
    },
]



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная', navmenu=navmenu)

@app.route('/account')
def account():
    return render_template('account.html', title='Аккаунт', navmenu=navmenu)

@app.route('/whatnew')
def whatnew():
    return render_template('whatnew.html', title='Что нового', navmenu=navmenu)

@app.route('/color')
def color():
    return render_template('color.html', title='Цвет', navmenu=navmenu)

@app.route('/order')
def order():
    return render_template('order.html', title='Заказ', navmenu=navmenu)



#Получаем все записи contactrequests из БД
@app.route('/api/contactrequest', methods=['GET'])
def get_contact_req_all():
    response = dbservice.get_contact_req_all()
    return json_response(response)

@app.route('/api/contactrequest/<int:id>', methods=['GET'])
# Получаем запись по id
def get_contact_req_by_id(id):
    response = dbservice.get_contact_req_by_id(id)
    return json_response(response)

@app.route('/api/contactrequest/author/<string:firstname>', methods=['GET'])
# Получаем запись по имени пользователя
def get_contact_req_by_author(firstname):
    if not firstname:
        # то возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
        # Иначе отправляем json-ответ
    else:
        response = dbservice.get_contact_req_by_author(firstname)
    return json_response(response)






@app.route('/api/contactrequest', methods=['POST'])
def create_contact_req():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в этом объекте нет, например, обязательного поля 'firstname'
    if not request.json or not 'firstname':
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе отправляем json-ответ
    else:
        msg = request.json['firstname'] + ", ваш запрос получен !";
        response = dbservice.create_contact_req(request.json)
        return json_response(response)



@app.route('/api/contactrequest/<int:id>', methods=['PUT'])
# Обработка запроса на обновление записи в БД
def update_contact_email_by_id(id):
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    if not request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе обновляем запись в БД и отправляем json-ответ
    else:
        response = dbservice.update_contact_email_by_id(id, request.json)
        return json_response(response)


@app.route('/api/contactrequest/<int:id>', methods=['DELETE'])
# Обработка запроса на удаление записи в БД по id
def delete_contact_req_by_id(id):
    response = dbservice.delete_contact_req_by_id(id)
    return json_response(response)




# Возврат html-страницы с кодом 404 (Не найдено)
@app.route('/notfound')
def not_found_html():
    return render_template('404.html', title='404', err={ 'error': 'Not found', 'code': 404 })

# Формирование json-ответа. Если в метод передается только data (dict-объект), то по-умолчанию устанавливаем код возврата code = 200
# В Flask есть встроенный метод jsonify(dict), который также реализует данный метод (см. пример метода not_found())
def json_response(data, code=200):
    return Response(status=code, mimetype="application/json", response=json.dumps(data))

# Пример формирования json-ответа с использованием встроенного метода jsonify()
# Обработка ошибки 404 протокола HTTP (Данные/страница не найдены)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)

# Обработка ошибки 400 протокола HTTP (Неверный запрос)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)
