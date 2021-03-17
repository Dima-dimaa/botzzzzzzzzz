try:
    import vk_api, requests, time, threading, filemath, os
    from vk_api.longpoll import VkLongPoll, VkEventType
    from vk_api.utils import get_random_id
    from vk_api.keyboard import VkKeyboard, VkKeyboardColor
    
    
    print("Бот запущен!")
    keyboard = VkKeyboard(one_time=False)
    # 1
    keyboard.add_button('Розыгрыши 🎉', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Баланс 💰', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Пополнить 💳', color=VkKeyboardColor.PRIMARY)
    
    clava2 = VkKeyboard(one_time=False)
    clava2.add_button('Оплата Qiwi 🥝', color=VkKeyboardColor.PRIMARY)
    clava2.add_line()
    clava2.add_openlink_button('Другие-способы', link='https://vk.com/prankbot3?w=app6887721_-203225016')
    clava2.add_line()
    clava2.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)
    
    clava3 = VkKeyboard(one_time=False)
    clava3.add_button('№1', color=VkKeyboardColor.SECONDARY)
    clava3.add_button('№2', color=VkKeyboardColor.SECONDARY)
    clava3.add_line()
    clava3.add_button('№3', color=VkKeyboardColor.SECONDARY)
    clava3.add_button('№4', color=VkKeyboardColor.SECONDARY)
    clava3.add_line()
    clava3.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)
    
    clava4 = VkKeyboard(one_time=False)
    clava4.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)
    
    
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
    api_access_token = 'df90a034743dca3538423874f14a78c0'
    
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
    
    
    
    
    def write_message(sender, message):
        if i == 1:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                                       'keyboard': keyboard.get_keyboard()})
        if i == 2:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                               'keyboard': clava2.get_keyboard()})
        if i == 3:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "attachment": "audio574170405_456239051,audio574170405_456239053,audio574170405_456239054,audio574170405_456239055", "random_id": get_random_id(),
                                               'keyboard': clava3.get_keyboard()})
        if i == 4:
            authorize.method('messages.send', {'user_id': sender, 'message': message,"random_id": get_random_id(),
                                               'keyboard': clava4.get_keyboard()})
    
    def xxx():
        while True:
            time.sleep(1500)
            write_message(592697054, 'ou')
    
    dd = threading.Thread(target=xxx)
    dd.start()
    
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
                        with open(str(user) + "c.txt", "r") as ca:
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
    
    token = "58be38fe16c679b894c6b7c0d42397a26d87b8a1944a1a3c38f883fd0df885bd16155de4d5d8ca9648c53"
    authorize = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(authorize)
    admin = 574170405
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
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
    
            if reseived_message == 'начать' and i == 1 \
                    or reseived_message == 'начать' and i == 1 \
                    or reseived_message == 'привет' and i == 1\
                    or reseived_message == 'ку' and i == 1 \
                    or reseived_message == 'хай' and i == 1 \
                    or reseived_message == 'здравствуйте' and i == 1 \
                    or reseived_message == 'start' and i == 1 \
                    or reseived_message == 'дарова' and i == 1:
                if check(sender) == 0:
                    adder(sender)
                    try:
                        a = open(str(sender) + ".txt", "r")
                        a.close()
                    except:
                        a = open(str(sender) + ".txt", "w")
                        a.write("0")
                        a.close()
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                write_message(sender, "Привет " + name + '! \nРады видеть тебя в нашей группе 😊')
                write_message(sender, 'Вы в главном меню: \n\n- Розыгрыши \n- Баланс \n- Пополнить')
            elif reseived_message == '№1' and i == 3:
                a = open(str(event.user_id) + "roz.txt", "w")
                a.write("1")
                a.close()
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("4")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Введите номер: \nПример: 79283335577')
            elif reseived_message == '№2' and i == 3:
                a = open(str(event.user_id) + "roz.txt", "w")
                a.write("2")
                a.close()
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("4")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Введите номер: \nПример: 79283335577')
            elif reseived_message == '№3' and i == 3:
                a = open(str(event.user_id) + "roz.txt", "w")
                a.write("3")
                a.close()
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("4")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Введите номер: \nПример: 79283335577')
            elif reseived_message == '№4' and i == 3:
                a = open(str(event.user_id) + "roz.txt", "w")
                a.write("4")
                a.close()
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("4")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Введите номер: \nПример: 79283335577')
            elif reseived_message[0:2] == "79" and len(reseived_message) == 11 and i == 4:
                with open(str(event.user_id) + "roz.txt", "r") as ro:
                    roz = ro.read()
                    roz = int(roz)
                try:
                    a = open(str(event.user_id) + ".txt", "r")
                    a.close()
                except:
                    a = open(str(event.user_id) + ".txt", "w")
                    a.write("0")
                    a.close()
                with open(str(event.user_id) + ".txt", "r") as ba2:
                    bal2 = ba2.read()
                    bal2 = int(bal2)
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("1")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                if bal2 >= 5:
                    if roz == 1:
                        requests.post(f'https://zvonok.com/manager/cabapi_external/api/v1/phones/call/?campaign_id=1211100981&phone=%2B{reseived_message}&public_key=eea63e1f9e02ece1871846f4ab8357ac')
                    if roz == 2:
                        requests.post(f'https://zvonok.com/manager/cabapi_external/api/v1/phones/call/?campaign_id=284357753&phone=%2B{reseived_message}&public_key=eea63e1f9e02ece1871846f4ab8357ac')
                    if roz == 3:
                        requests.post(f'https://zvonok.com/manager/cabapi_external/api/v1/phones/call/?campaign_id=1082629254&phone=%2B{reseived_message}&public_key=eea63e1f9e02ece1871846f4ab8357ac')
                    if roz == 4:
                        requests.post(f'https://zvonok.com/manager/cabapi_external/api/v1/phones/call/?campaign_id=1803128821&phone=%2B{reseived_message}&public_key=eea63e1f9e02ece1871846f4ab8357ac')
                    a = open(str(sender) + ".txt", "w")
                    a.write(str(int(bal2) - int(str(5))))
                    a.close
                    write_message(sender, f'Звонок отправлен ✅ \nНомер - {reseived_message} 😇')
                else:
                    write_message(sender, 'У вас недостаточно средств :(')
            elif reseived_message[0:5] == 'admin':
                write_message(sender, 'Уже позвал Админа :) \nЖдите ответ в течении 1 - часа !!!')
                write_message(574170405, 'Зовут')            
            elif reseived_message[0:9] == 'розыгрыши':
                try:
                    a = open(str(sender) + ".txt", "r")
                    a.close()
                except:
                    a = open(str(sender) + ".txt", "w")
                    a.write("0")
                    a.close()
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("3")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Выберите номер розыгрыша 🎉 \nЦена: 5 руб - 1 звонок ☎')
            elif reseived_message[0:6] == "баланс":
                try:
                    a = open(str(event.user_id) + ".txt", "r")
                    a.close()
                except:
                    a = open(str(event.user_id) + ".txt", "w")
                    a.write("0")
                    a.close()
                with open(str(event.user_id) + ".txt", "r") as ba2:
                    bal2 = ba2.read()
                    bal2 = int(bal2)
                write_message(sender, "Твой баланс: " + str(bal2) + " руб.")
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
                              'Qiwi-кошелёк: +79283692011 \nНе забудьте указать этот код в комментариях к платежу: ' + "1" + str(
                                  sender) + ' ❗ '
                                            '\n\nПосле оплаты на ваш баланс автоматически в течении минуты будет зачисленна сумма перевода, если оплата придет вам сообщат')
            elif reseived_message[0:5] == 'назад' and i == 2 or reseived_message[0:5] == 'назад' and i == 3:
                a = open(str(sender) + "c.txt", "w")
                a.write("1")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Вы в главном меню: \n\n- Розыгрыши \n- Баланс \n- Пополнить')
            elif reseived_message[0:5] == 'назад' and i == 4:
                a = open(str(sender) + "c.txt", "w")
                a.write("3")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, "Выберите номер розыгрыша 🎉")
            elif reseived_message[0:2] == "фф":
                if sender == 574170405:
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
                if i == 1:
                    write_message(sender, 'Вы в главном меню: \n\n- Розыгрыши \n- Баланс \n- Пополнить')
                if i == 2:
                    write_message(sender, 'Пожалуйста используйте кнопки:')
                if i == 3:
                    write_message(sender, 'Выберите вариант с помощью кнопок:')
                if i == 4:
                    write_message(sender, 'Не верно !!! \nВведите номер: \nПример: 79283335577')
except:
    os.system('python bot.py')
