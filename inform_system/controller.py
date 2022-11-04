import logger
import model
import ui

while True:
    mode = model.typeAction()
    if mode == 1:
        logger.writeData(ui.getData())
    elif mode == 2:
        cont = model.getRequest()
        direct = logger.logDirect()
        print(model.searchContact(direct, cont))
    elif mode == 3:
        base = logger.logDirect()
        newBase = model.editing (base)
        logger.writeEdited (newBase)
    elif mode == 0:
        print('Выход')
        break
    else:
        print('Выберете вариант действий из предложенных')