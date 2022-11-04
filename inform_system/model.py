# изменение и поиск
import random

def searchData():
    with open('base.txt', 'r',  encoding='utf-8') as base:
        userData = input('Введите данные для поиска: ')
        for i in base:
            if i.find(userData) != -1:
                return i

def getRequest():
    return input('Введите данные сотрудника: ')

def typeAction():
    return int(input('Для добавления нового сотрудника введите - 1; для поиска - 2; для редактирования - 3\n'))

def searchContact(direct: list, cont: str) -> str:
    z = ''
    for i in direct:
        if i.find(cont) != -1:
            z = i
    if z == '':
        return "Контакт не найден"
    else:
        return z

def editing(mass):
    a = input('Редакировать информацию о сотруднике: ')
    staff = []
    index = 0
    for i in range(len(mass)):
        if mass[i].find(a) != -1:
            staff = mass[i].split('||')
            print(staff)
            index = i
    print(f'Выберите параметр для редактиования:\n \
        {staff[1]} - 1\n \
        {staff[2]} - 2\n \
        {staff[3]} - 3\n \
        {staff[4]} - 4\n \
        {staff[5]} - 5\n ')
    atribute = int(input())
    staff[atribute] = input('Введите новое значение: ')
    staff = '||'.join(staff)
    mass[index] = staff
    return mass