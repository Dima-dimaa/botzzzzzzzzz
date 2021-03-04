import vk_api, requests, time, threading, filemath, pathlib, os
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from SimpleQIWI import *


keyboard = VkKeyboard(one_time=False)
# 1
keyboard.add_button('Купить акк ??', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Продать акк ??', color=VkKeyboardColor.NEGATIVE)
keyboard.add_line()
keyboard.add_button('Баланс ??', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Пополнить ??', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Вывод ??', color=VkKeyboardColor.SECONDARY)

clava2 = VkKeyboard(one_time=False)
clava2.add_button('Оплата Qiwi ??', color=VkKeyboardColor.PRIMARY)
clava2.add_line()
clava2.add_button('Назад ?', color=VkKeyboardColor.SECONDARY)

clava3 = VkKeyboard(one_time=False)
clava3.add_button('Назад ?', color=VkKeyboardColor.SECONDARY)

clava4 = VkKeyboard(one_time=False)
clava4.add_button('Меню ??', color=VkKeyboardColor.NEGATIVE)
clava4.add_line()
clava4.add_button('Назад ?', color=VkKeyboardColor.SECONDARY)
clava5 = VkKeyboard(one_time=False)
clava5.add_button('Купить аккаунт ??', color=VkKeyboardColor.PRIMARY)
clava5.add_line()
clava5.add_button('Информация об аккаунте ?', color=VkKeyboardColor.PRIMARY)
clava5.add_line()
clava5.add_button('Назад ?', color=VkKeyboardColor.SECONDARY)
clava6 = VkKeyboard(one_time=False)
clava6.add_button('Назад ?', color=VkKeyboardColor.SECONDARY)
clava7 = VkKeyboard(one_time=False)
clava7.add_button('Назад ?', color=VkKeyboardColor.SECONDARY)
clava8 = VkKeyboard(one_time=False)
clava8.add_button('Назад ?', color=VkKeyboardColor.SECONDARY)
clava9 = VkKeyboard(one_time=False)
clava9.add_button('VK', color=VkKeyboardColor.PRIMARY)
clava9.add_line()
clava9.add_button('Назад ?', color=VkKeyboardColor.SECONDARY)
clava10 = VkKeyboard(one_time=False)
clava10.add_button('Назад ?', color=VkKeyboardColor.SECONDARY)

def check(x):
    file = open('baza.txt', 'r', encoding='utf-8')
    if str(x) in file.read():
        return 1
    else:
        return 0
    file.close()


def adder(x):
    file = open('baza.txt', 'a', encoding='utf-8')
    file.write(f'{x}\n')

    file.close()


UsersId = open("baza.txt", "r")
UsersId2 = set()
for line in UsersId:
    UsersId2.add(line.strip())
UsersId.close()

suser = []
for user in UsersId2:
    suser.append(str(user))


def extract_aarg(aarg):
    return aarg.split()[0]

def extract_arg(arg):
    return arg.split()[1]

def extract_arg2(arg2):
    return arg2.split()[2]


def payment_history_last(my_login, api_access_token, rows_num, next_TxnId, next_TxnDate):
    # сессия для рекуест
    s = requests.Session()
    # добавляем рекуесту headers
    s.headers['authorization'] = 'Bearer ' + api_access_token
    # параметры
    parameters = {'rows': rows_num, 'nextTxnId': next_TxnId, 'nextTxnDate': next_TxnDate}
    # через рекуест получаем платежы с параметрами - parameters
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params=parameters)
    # обязательно json все объекты в киви апи json
    return h.json()


mylogin = '79283692011'
api_access_token = '28540e35aa5c152017cec0f4340a4569'


def QiwiCheck(number, api):
    while True:
        time.sleep(30)
        lastPayments = payment_history_last(number, api, '1', '', '')

        num = lastPayments['data'][0]['account']
        sum = lastPayments['data'][0]['sum']['amount']
        comm = lastPayments['data'][0]['comment']
        type = lastPayments['data'][0]['type']
        txnId = lastPayments['data'][0]['txnId']
        txnId = str(txnId)

        a = open("thlp.txt", "r")
        lastpay = a.read()
        lastpay = str(lastpay)
        a.close()

        if lastpay == txnId:
            pass
        else:
            try:
                a = open(str(comm[1:]) + ".txt", "r")
                a.close()
                filemath.pmms(str(comm[1:]) + ".txt", "+" + str(sum))

                a = open("thlp.txt", 'w')
                a.write(txnId)
                a.close()

                write_message(int(comm[1:]), "На ваш баланс зачисленно " + str(sum) + "р\n\nУдачных покупок!")

            except:
                pass

Tqiwi = threading.Thread(target=QiwiCheck, args=(mylogin, api_access_token))
Tqiwi.start()


    # authorize.method('messages.send', {'user_id': sender, 'sticker_id': 75, "random_id": get_random_id()})
def write_message(sender, message):
    if i == 1:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': keyboard.get_keyboard()})
    if i == 2:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava2.get_keyboard()})
    if i == 3:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava3.get_keyboard()})
    if i == 4:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava4.get_keyboard()})
    if i == 5:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava5.get_keyboard()})
    if i == 6:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava6.get_keyboard()})
    if i == 7:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava7.get_keyboard()})
    if i == 8:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava8.get_keyboard()})
    if i == 9:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava9.get_keyboard()})
    if i == 10:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava10.get_keyboard()})

def rass(soob, xui, govno, jopa):
    if 1 == 1:
        UsersId = open("baza.txt", "r")
        UsersId2 = set()
        for line in UsersId:
            UsersId2.add(line.strip())
        UsersId.close()

        suser = []
        for user in UsersId2:
            suser.append(str(user))
        if a == 1:
            succes = 0
            fail = 0
            for user in suser:
                try:
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(int(user), sms)
                    succes += 1
                except:
                    fail += 1
                    continue
            so_ob = "none"
            write_message("574170405", "Рассылку получило - " + str(succes) + " пользователей")
            write_message("574170405", "Заблокировали бота - " + str(fail) + " пользователей")


token = "9b720406d3ce593777a5fdb31c18b07a74ad8207ef1ff8ff85d41ecd932c5e4b8dd3c793d76e3f91e7524"
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)
admin = [574170405]
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        try:
            a = open(str(event.user_id) + "c.txt", "r")
            a.close()
        except:
            a = open(str(event.user_id) + "c.txt", "w")
            a.write("1")
            a.close()
        with open(str(event.user_id) + "c.txt", "r") as ca:
            i = ca.read()
            i = int(i)
        reseived_message = event.text.lower()
        sender = event.user_id
        user = authorize.method("users.get", {"user_ids": event.user_id})  # вместо 1 подставляете айди нужного юзера
        name = user[0]['first_name']

        if reseived_message == 'начать' \
                or reseived_message == 'привет' \
                or reseived_message == 'ку' \
                or reseived_message == 'хай' \
                or reseived_message == 'здравствуйте' \
                or reseived_message == 'дарова':
            if check(sender) == 0:
                adder(sender)

            a = open(str(event.user_id) + "c.txt", "w")
            a.write("1")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            try:
                a = open(str(sender) + ".txt", "r")
                a.close()
            except:
                a = open(str(sender) + ".txt", "w")
                a.write("0")
                a.close()

            write_message(sender, "Выбери:")
        elif reseived_message[0:22] == 'информация об аккаунте' and i == 5:
            a = open(str(event.user_id) + "c.txt", "w")
            a.write("7")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, 'Введите код аккаунта для получения информации:')
        elif reseived_message[0:14] == 'купить аккаунт' and i == 5:
            a = open(str(event.user_id) + "c.txt", "w")
            a.write("6")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, 'Введите код аккаунта:')
        elif reseived_message[0:10] == "купить акк" and i == 1:
            a = open(str(event.user_id) + "c.txt", "w")
            a.write("5")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, 'Выбери:')
        elif reseived_message[0:11] == "продать акк" and i == 1:
            try:
                open(str(event.user_id) + "ac.txt", "r")
                open(str(event.user_id) + "acc.txt", "r")
                write_message(sender,f'У вас уже есть аккаунт на продаже !!! \nДля отмены напишите: \nОтмена {sender}')
            except:
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("9")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Выберите тип аккаунта:')

        elif reseived_message[0:2] == "vk" and i == 9:
            a = open(str(sender) + "vk.txt", "w")
            a.write("1")
            a.close()
            a = open(str(event.user_id) + "c.txt", "w")
            a.write("3")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender,
                          'Пожалуйста расскажите о вашем аккаунте перед продажей: \n\n- Что это за аккаунт ?\n- Какие у него плюсы ?'
                          '\nСтоимость вы укажите позже, после описания :)')
        elif reseived_message[0:5] == "вывод" and i == 1:
            write_message(sender,
                          "Введите номер Qiwi и сумму вывода ?? \nПример: \n+79283335522 50 \n+77074470707 75 \n+380443777355 100 \n+375297556655 150 \nКомиссия за вывод 10 - %")
        elif reseived_message[0:3] == "+79" and i == 1\
                or reseived_message[0:3] == "+77" and i == 1 \
                or reseived_message[0:4] == "+380" and i == 1 \
                or reseived_message[0:4] == "+375" and i == 1:
            try:
                deen = extract_aarg(reseived_message)
                den = extract_arg(reseived_message)
                try:
                    a = open(str(sender) + ".txt", "r")
                    a.close()
                except:
                    a = open(str(sender) + ".txt", "w")
                    a.write('0')
                    a.close()
                with open(str(event.user_id) + ".txt", "r") as ba2:
                    bal2 = ba2.read()
                    bal2 = int(bal2)
                    print(den)
                if bal2 >= int(den):
                    print(den)
                    user = authorize.method("users.get", {"user_ids": sender})
                    fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
                    if int(den) >= 35:
                        a = open(str(event.user_id) + ".txt", "w")
                        a.write(str(int(bal2) - int(str(den))))
                        a.close()
                        den = int(den) - (int(den) * 0.1)

                        token = '28540e35aa5c152017cec0f4340a4569'
                        phone = '79283692011'
                        print('1 так')
                        api = QApi(token=token, phone=phone)
                        print('2 так')
                        api.pay(account=str(deen), amount=str(den), comment="Покупка - продажа аккаунтов !!!")
                        print('3 так')

                        write_message(sender,
                                      f"Ожидайте вывод в течении: \n5 - минут !!! \nСумма к начислению: {den} руб.")
                        write_message(574170405,
                                      f"Новый вывод! \n[https://vk.com/id{sender}|{fullname}] \nСумма: {den}")
                    else:
                        write_message(sender, 'Сумма не может быть меньше 35 руб !!!')
                else:
                    write_message(sender, 'У вас нет таких денег !!!')
            except:
                write_message(sender, 'Не верные данные!')
        elif reseived_message[0:6] == "баланс":
            try:
                a = open(str(event.user_id) + ".txt", "r")
                a.close()
            except:
                a = open(str(event.user_id) + ".txt", "w")
                a.write("0")
                a.close()
            with open(str(sender) + ".txt", "r") as ba:
                bal = ba.read()
                bal == str(bal)
            write_message(sender, "Ваш текущий баланс: " + bal + " руб.")
        elif reseived_message[0:4] == 'меню' and i == 4 or reseived_message[0:4] == 'меню' and i == 10:
            a = open(str(sender) + "c.txt", "w")
            a.write("1")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            file = pathlib.Path(f"{sender}ac.txt")
            file.unlink()
            write_message(sender, "Выбери:")
        elif reseived_message[0:5] == 'назад' and i == 4:
            a = open(str(sender) + "c.txt", "w")
            a.write("3")
            a.close()
            try:
                file = pathlib.Path(f"{sender}ac.txt")
                file.unlink()
            except:
                pass
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender,
                          'Пожалуйста расскажите о вашем аккаунте перед продажей: \n\n- Что это за аккаунт ?\n- Каие у него плюсы ?'
                          '\nСтоимость вы укажите позже, после описания :)')
        elif reseived_message[0:5] == 'назад' and i == 6 or \
                reseived_message[0:5] == 'назад' and i == 7:
            a = open(str(sender) + "c.txt", "w")
            a.write("5")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "Выбери:")
        elif reseived_message[0:6] == "отмена":
            smd = extract_arg(reseived_message)
            if int(smd) == sender:
                try:
                    file = pathlib.Path(f"{smd}ac.txt")
                    file.unlink()
                    write_message(event.user_id, "Аккаунт удалён !!!")
                except:
                    write_message(event.user_id, "У вас нет аккаунтов на продаже !!!")
            else:
                write_message(event.user_id, "Не верный код !!!")
        elif reseived_message[0:5] == 'назад' and i == 3:
            try:
                file = pathlib.Path(f"{sender}ac.txt")
                file.unlink()
            except:
                pass
            a = open(str(sender) + "c.txt", "w")
            a.write("9")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "Выбери:")
        elif reseived_message[0:5] == 'назад' and i == 10:
            a = open(str(sender) + "c.txt", "w")
            a.write("8")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "Введите логин:")
        elif reseived_message[0:5] == 'назад' and i == 8:
            a = open(str(sender) + "c.txt", "w")
            a.write("4")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, 'Отлично укажите сумму: \nПример: 25')
        elif reseived_message[0:5] == 'назад' and i == 2 or \
                reseived_message[0:5] == 'назад' and i == 9 or \
                reseived_message[0:5] == 'назад' and i == 5:
            a = open(str(sender) + "c.txt", "w")
            a.write("1")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "Выбери:")
        elif reseived_message[0:8] == "рассылка":
            if sender == 574170405:
                a = 0
                try:
                    sm = extract_arg(event.text)
                    a = 1
                except:
                    write_message(event.user_id, "Вы не указали текст для рассылки")
                if a == 1:
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(event.user_id, "Рссылка началась")
                    sms = event.text[8:]
                    so_ob = sms
                    t = threading.Thread(target=rass, args=(sms, 1, 2, 3))
                    t.start()
                else:
                    write_message(sender, 'Вы не являетесь администратором !!!')
        elif reseived_message[0:9] == "пополнить":
            a = open(str(event.user_id) + "c.txt", "w")
            a.write("2")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "Выберите способ оплаты")
        elif reseived_message[0:11] == "оплата qiwi" and i == 2:
                write_message(sender,
                              'Qiwi-кошелёк: +79283692011 \nНе забудьте указать этот код в комментариях к платежу: ' + "1" + str(sender) + ' ? '
                                            '\n\nПосле оплаты на ваш баланс автоматически в течении минуты будет зачисленна сумма перевода, если оплата придет вам сообщат')
        elif reseived_message[0:2] == "фф":
            if sender == 574170405 or sender == 554311036:
                try:
                    id = extract_arg(reseived_message)
                    bal = extract_arg2(reseived_message)
                    a = open(str(id) + ".txt", "r")
                    skoko = a.read()
                    skoko = int(skoko)
                    a.close()
                    a = open(str(id) + ".txt", "w")
                    a.write(str(skoko + int(bal)))
                    a.close()
                    write_message(event.user_id, "Готово")
                    write_message(str(id), "На ваш баланс зачислено " + str(bal) + " руб.")
                except:
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                    write_message(event.user_id, "Вы не указали айди или сумму")
            else:
                with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                write_message(sender, 'Вы не являетесь администратором !!!')
        else:
            if i == 3:
                a = open(str(event.user_id) + "ac.txt", "w", encoding='utf-8')
                a.write(f'{event.text}')
                a.close()
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("4")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Отлично укажите сумму: \nПример: 25')
            elif i == 6:
                try:
                    with open(str(sender) + "pass.txt", "r") as pa:
                        pas = pa.read()
                        pas == str(pas)
                    with open(str(reseived_message) + "acc.txt", "r") as cvv:
                        ddd = cvv.read()
                        ddd == str(ddd)
                    with open(str(reseived_message) + "ac.txt", "r", encoding='utf-8') as cv:
                        dd = cv.read()
                        dd == str(dd)
                    with open(str(sender) + ".txt", "r") as ba:
                        bal = ba.read()
                        bal == str(bal)
                    with open(str(reseived_message) + "aac.txt", "r", encoding='utf-8') as ccv:
                        cdd = ccv.read()
                        cdd == str(cdd)
                    print(ddd)
                    print(bal)
                    ss = requests.get(
                        f"https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username={cdd}&password={pas}")
                    if str(ss) == '<Response [200]>':
                        if int(bal) >= int(ddd):
                            print(bal + 'c')
                            with open(str(sender) + ".txt", "r") as ba:
                                bal = ba.read()
                                bal == str(bal)
                            a = open(str(sender) + ".txt", "w")
                            a.write(str(int(bal) - int(str(ddd))))
                            a.close
                            print(bal + 'cg')
                            with open(str(sender) + ".txt", "r") as ba:
                                bal = ba.read()
                                bal == str(bal)
                            a = open(str(event.user_id) + "c.txt", "w")
                            a.write("1")
                            a.close()
                            with open(str(reseived_message) + ".txt", "r") as ba:
                                bal = ba.read()
                                bal == str(bal)
                            a = open(str(reseived_message) + ".txt", "w")
                            a.write(str(int(bal) + int(str(ddd))))
                            a.close
                            with open(str(sender) + ".txt", "r") as ba:
                                bal = ba.read()
                                bal == str(bal)
                            write_message(str(reseived_message), "Ваш аккаунт купили :)")
                            write_message(str(reseived_message), "На ваш баланс зачислено " + str(ddd) + " руб.")
                            file = pathlib.Path(str(reseived_message) + "ac.txt")
                            file.unlink()
                            file = pathlib.Path(str(reseived_message) + "aac.txt")
                            file.unlink()
                            file = pathlib.Path(str(reseived_message) + "acc.txt")
                            file.unlink()
                            with open(str(event.user_id) + "c.txt", "r") as ca:
                                i = ca.read()
                                i = int(i)
                            write_message(sender, f'Логин: {cdd} \nПароль: {pas}')
                            write_message(sender, 'Поздравляем с покупкой :)')
                        else:
                            write_message(sender, 'У вас недостаточно средств !!!')
                    else:
                        write_message(sender, 'Хм.. \nНе верный логин или пароль !!!')
                        file = pathlib.Path(str(reseived_message) + "ac.txt")
                        file.unlink()
                        file = pathlib.Path(str(reseived_message) + "aac.txt")
                        file.unlink()
                        file = pathlib.Path(str(reseived_message) + "acc.txt")
                        file.unlink()
                        write_message((str(reseived_message)), 'У вас не верный логин или пароль !!! \nПокупатель не смог купить ваш аккаунт :(')
                except:
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                    write_message(sender, 'Аккаунт не найден :(')
            elif i == 8:
                a = open(str(event.user_id) + "aac.txt", "w", encoding='utf-8')
                a.write(f'{event.text}')
                a.close()
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("1")
                a.close()
                a = open(str(event.user_id) + "login.txt", "w")
                a.write(str(reseived_message))
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("10")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Введите пароль:')
            elif i == 7:
                try:
                    user = authorize.method("users.get", {"user_ids": reseived_message})
                    fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
                    with open(str(reseived_message) + "ac.txt", "r", encoding='utf-8') as cv:
                        dd = cv.read()
                        dd == str(dd)
                    with open(str(reseived_message) + "acc.txt", "r") as cvv:
                        ddd = cvv.read()
                        ddd == str(ddd)
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                    write_message(sender, f'Информация об аккаунте ?\nСоздал: [https://vk.com/id{reseived_message}|{fullname}] ?? \n\n{dd}\n\nЦена: {ddd} руб.')
                except:
                    write_message(sender, 'Информации об аккаунте: \nНе найдено :(')
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
            elif i == 10:
                try:
                    with open(str(event.user_id) + "login.txt", "r") as cda:
                        iq = cda.read()
                        iq = int(iq)
                    ss = requests.get(f"https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username={iq}&password={event.text}")
                    if str(ss) == '<Response [200]>':
                        a = open(str(event.user_id) + "c.txt", "w")
                        a.write("1")
                        a.close()
                        a = open(str(event.user_id) + "pass.txt", "w", encoding='utf-8')
                        a.write(f'{event.text}')
                        a.close()
                        with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                        write_message(sender,
                                      f'Ваш аккаунт опубликован ? \nВаш код: {sender} \nМожете рассказать о нём здесь:\nhttps://vk.com/topic-202416186_46921809'
                                      f'\nНо не забудьте добавить код чтобы у вас смогли купить его !!!')
                    else:
                        write_message(sender,'Не верный логин или пароль !!!')
                except:
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(sender, 'Что-то пошло не так :( \nПопробуйте ещё раз !!!')
            elif i == 4:
                try:
                    if int(event.text) > 0:
                        dj = 0
                        qq = (str(int(event.text) + int(str(dj))))
                        a = open(str(event.user_id) + "c.txt", "w")
                        a.write("8")
                        a.close()
                        with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                        a = open(str(event.user_id) + "acc.txt", "w")
                        a.write(qq)
                        a.close()
                        write_message(sender, 'Введите логин:')
                    else:
                        write_message(sender, 'Сумма должна быть больше 0 !!!')
                except:
                    write_message(sender, f'"{reseived_message}" не является числом !!!')
            else:
                with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                write_message(sender, 'Я тя не понял :/')