# for CRUD operations

from appiphnoe import db
from datetime import datetime
from sqlalchemy import text
from flask import session, make_response, redirect, url_for, jsonify
import bcrypt



# Получаем запрос с фильтром по id
def get_contact_req_by_id(id):
    stmt = text(f"SELECT * FROM orderrequests WHERE id = {id}")
    result = db.session.execute(stmt).fetchone()
    if result:
        return dict(result._asdict())
    else:
        return None



# Получаем список всех запросов.
def get_contact_req_all():
    try:
        result = []  # создаем пустой список
        # Получаем итерируемый объект, где содержатся все строки таблицы orderrequests
        stmt = text("SELECT * FROM orderrequests")
        rows = db.session.execute(stmt).fetchall()
        # Каждую строку конвертируем в словарь
        for row in rows:
            row_dict = dict(row._mapping.items())
            result.append(row_dict)
        # Возвращаем словарь с ключом 'orderrequests', где значение - это список словарей с информацией
        return {'orderrequests': result}
    except Exception as e:
        # Обработка ошибок
        return {'error': str(e)}



# Получаем все запросы по имени автора
def get_contact_req_by_author(firstname):
    result = []
    stmt = text(f"SELECT * FROM orderrequests WHERE firstname = '{firstname}'")
    rows = db.session.execute(stmt).fetchall()
    for row in rows:
        row_dict = dict(row._mapping.items())
        result.append(row_dict)
        # result.append(dict(row))
    return {'orderrequests': result}





# Создать новый запрос
def create_contact_req(json_data):
    try:
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")     # текущая дата и время

        # Используйте text() для объявления текстового SQL-выражения
        stmt = text("INSERT INTO orderrequests (firstName, lastName, phone, email, createdAt, updatedAt) "
                    "VALUES (:firstname, :lastName, :phone, :email, :createdAt, :updatedAt)")

        # Выполните SQL-выражение с использованием параметров
        db.session.execute(stmt, {
            'firstname': json_data['firstname'],
            'lastName': json_data['lastname'],
            'phone': json_data['phone'],
            'email': json_data['email'],
            'createdAt': cur_time,
            'updatedAt': cur_time
        })

        # Подтвердите изменения в БД
        db.session.commit()

        # Возвращаем результат
        return {'message': "OrderRequest Created!"}

    except Exception as e:
        # Откатываем изменения в БД
        db.session.rollback()
        # Возвращаем dict с ключом 'error' и текстом ошибки
        return {'message': str(e)}





# Удалить запрос по id в таблице
def delete_contact_req_by_id(id):
    try:
        # DELETE запрос в БД
        stmt = text(f"DELETE FROM orderrequests WHERE id = {id}")
        db.session.execute(stmt)
        db.session.commit()
        return {'message': "OrderRequest Deleted!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Обновить email запроса по id в таблице
def update_contact_email_by_id(id, json_data):
    try:
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # текущая дата и время
        # UPDATE запрос в БД
        stmt = text(f"UPDATE orderrequests SET email = '{json_data['email']}', "f"updatedAt = '{cur_time}' WHERE id = {id}")
        db.session.execute(stmt)
        db.session.commit()
        return {'message': "OrderRequest Updated!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

