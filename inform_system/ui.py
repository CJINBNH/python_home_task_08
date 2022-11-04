# ввод и вывод информации


def getData():
    id = input('ID сотрудника: ')
    surname = input('Введите Фамилию сотрудника: ')
    name = input('Введите Имя сотрудника: ')
    phone = input('Введите номер телефона сотрудника: ')
    post = input('Введите должность сотрудника: ')
    cost = input('Введите з/п сотрудника: ')
    return (f'{id} || {surname} || {name} || {phone} || {post} || {cost}')