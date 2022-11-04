# чтение и запись данных

def writeData(a):
    with open('base.txt', 'a',  encoding='utf-8') as base:
        base.write(f'{a} \n')

def logDirect():
    direct = []
    with open('base.txt', 'r', encoding='utf-8') as base:
        for line in base:
            direct.append(line)
    return direct

def writeEdited(mass):
    with open('base.txt', 'w', encoding='utf-8') as base:
        for i in mass:
            base.write(i)