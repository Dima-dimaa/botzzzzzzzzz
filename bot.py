import vk_api, requests, time, threading, filemath, pathlib, os
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from SimpleQIWI import *


keyboard = VkKeyboard(one_time=False)
# 1
keyboard.add_button('������ ��� ??', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('������� ��� ??', color=VkKeyboardColor.NEGATIVE)
keyboard.add_line()
keyboard.add_button('������ ??', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('��������� ??', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('����� ??', color=VkKeyboardColor.SECONDARY)

clava2 = VkKeyboard(one_time=False)
clava2.add_button('������ Qiwi ??', color=VkKeyboardColor.PRIMARY)
clava2.add_line()
clava2.add_button('����� ?', color=VkKeyboardColor.SECONDARY)

clava3 = VkKeyboard(one_time=False)
clava3.add_button('����� ?', color=VkKeyboardColor.SECONDARY)

clava4 = VkKeyboard(one_time=False)
clava4.add_button('���� ??', color=VkKeyboardColor.NEGATIVE)
clava4.add_line()
clava4.add_button('����� ?', color=VkKeyboardColor.SECONDARY)
clava5 = VkKeyboard(one_time=False)
clava5.add_button('������ ������� ??', color=VkKeyboardColor.PRIMARY)
clava5.add_line()
clava5.add_button('���������� �� �������� ?', color=VkKeyboardColor.PRIMARY)
clava5.add_line()
clava5.add_button('����� ?', color=VkKeyboardColor.SECONDARY)
clava6 = VkKeyboard(one_time=False)
clava6.add_button('����� ?', color=VkKeyboardColor.SECONDARY)
clava7 = VkKeyboard(one_time=False)
clava7.add_button('����� ?', color=VkKeyboardColor.SECONDARY)
clava8 = VkKeyboard(one_time=False)
clava8.add_button('����� ?', color=VkKeyboardColor.SECONDARY)
clava9 = VkKeyboard(one_time=False)
clava9.add_button('VK', color=VkKeyboardColor.PRIMARY)
clava9.add_line()
clava9.add_button('����� ?', color=VkKeyboardColor.SECONDARY)
clava10 = VkKeyboard(one_time=False)
clava10.add_button('����� ?', color=VkKeyboardColor.SECONDARY)

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
    # ������ ��� �������
    s = requests.Session()
    # ��������� �������� headers
    s.headers['authorization'] = 'Bearer ' + api_access_token
    # ���������
    parameters = {'rows': rows_num, 'nextTxnId': next_TxnId, 'nextTxnDate': next_TxnDate}
    # ����� ������� �������� ������� � ����������� - parameters
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params=parameters)
    # ����������� json ��� ������� � ���� ��� json
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

                write_message(int(comm[1:]), "�� ��� ������ ���������� " + str(sum) + "�\n\n������� �������!")

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
            write_message("574170405", "�������� �������� - " + str(succes) + " �������������")
            write_message("574170405", "������������� ���� - " + str(fail) + " �������������")


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
        user = authorize.method("users.get", {"user_ids": event.user_id})  # ������ 1 ������������ ���� ������� �����
        name = user[0]['first_name']

        if reseived_message == '������' \
                or reseived_message == '������' \
                or reseived_message == '��' \
                or reseived_message == '���' \
                or reseived_message == '������������' \
                or reseived_message == '������':
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

            write_message(sender, "������:")
        elif reseived_message[0:22] == '���������� �� ��������' and i == 5:
            a = open(str(event.user_id) + "c.txt", "w")
            a.write("7")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, '������� ��� �������� ��� ��������� ����������:')
        elif reseived_message[0:14] == '������ �������' and i == 5:
            a = open(str(event.user_id) + "c.txt", "w")
            a.write("6")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, '������� ��� ��������:')
        elif reseived_message[0:10] == "������ ���" and i == 1:
            a = open(str(event.user_id) + "c.txt", "w")
            a.write("5")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, '������:')
        elif reseived_message[0:11] == "������� ���" and i == 1:
            try:
                open(str(event.user_id) + "ac.txt", "r")
                open(str(event.user_id) + "acc.txt", "r")
                write_message(sender,f'� ��� ��� ���� ������� �� ������� !!! \n��� ������ ��������: \n������ {sender}')
            except:
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("9")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, '�������� ��� ��������:')

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
                          '���������� ���������� � ����� �������� ����� ��������: \n\n- ��� ��� �� ������� ?\n- ����� � ���� ����� ?'
                          '\n��������� �� ������� �����, ����� �������� :)')
        elif reseived_message[0:5] == "�����" and i == 1:
            write_message(sender,
                          "������� ����� Qiwi � ����� ������ ?? \n������: \n+79283335522 50 \n+77074470707 75 \n+380443777355 100 \n+375297556655 150 \n�������� �� ����� 10 - %")
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
                        print('1 ���')
                        api = QApi(token=token, phone=phone)
                        print('2 ���')
                        api.pay(account=str(deen), amount=str(den), comment="������� - ������� ��������� !!!")
                        print('3 ���')

                        write_message(sender,
                                      f"�������� ����� � �������: \n5 - ����� !!! \n����� � ����������: {den} ���.")
                        write_message(574170405,
                                      f"����� �����! \n[https://vk.com/id{sender}|{fullname}] \n�����: {den}")
                    else:
                        write_message(sender, '����� �� ����� ���� ������ 35 ��� !!!')
                else:
                    write_message(sender, '� ��� ��� ����� ����� !!!')
            except:
                write_message(sender, '�� ������ ������!')
        elif reseived_message[0:6] == "������":
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
            write_message(sender, "��� ������� ������: " + bal + " ���.")
        elif reseived_message[0:4] == '����' and i == 4 or reseived_message[0:4] == '����' and i == 10:
            a = open(str(sender) + "c.txt", "w")
            a.write("1")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            file = pathlib.Path(f"{sender}ac.txt")
            file.unlink()
            write_message(sender, "������:")
        elif reseived_message[0:5] == '�����' and i == 4:
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
                          '���������� ���������� � ����� �������� ����� ��������: \n\n- ��� ��� �� ������� ?\n- ���� � ���� ����� ?'
                          '\n��������� �� ������� �����, ����� �������� :)')
        elif reseived_message[0:5] == '�����' and i == 6 or \
                reseived_message[0:5] == '�����' and i == 7:
            a = open(str(sender) + "c.txt", "w")
            a.write("5")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "������:")
        elif reseived_message[0:6] == "������":
            smd = extract_arg(reseived_message)
            if int(smd) == sender:
                try:
                    file = pathlib.Path(f"{smd}ac.txt")
                    file.unlink()
                    write_message(event.user_id, "������� ����� !!!")
                except:
                    write_message(event.user_id, "� ��� ��� ��������� �� ������� !!!")
            else:
                write_message(event.user_id, "�� ������ ��� !!!")
        elif reseived_message[0:5] == '�����' and i == 3:
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
            write_message(sender, "������:")
        elif reseived_message[0:5] == '�����' and i == 10:
            a = open(str(sender) + "c.txt", "w")
            a.write("8")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "������� �����:")
        elif reseived_message[0:5] == '�����' and i == 8:
            a = open(str(sender) + "c.txt", "w")
            a.write("4")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, '������� ������� �����: \n������: 25')
        elif reseived_message[0:5] == '�����' and i == 2 or \
                reseived_message[0:5] == '�����' and i == 9 or \
                reseived_message[0:5] == '�����' and i == 5:
            a = open(str(sender) + "c.txt", "w")
            a.write("1")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "������:")
        elif reseived_message[0:8] == "��������":
            if sender == 574170405:
                a = 0
                try:
                    sm = extract_arg(event.text)
                    a = 1
                except:
                    write_message(event.user_id, "�� �� ������� ����� ��� ��������")
                if a == 1:
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(event.user_id, "������� ��������")
                    sms = event.text[8:]
                    so_ob = sms
                    t = threading.Thread(target=rass, args=(sms, 1, 2, 3))
                    t.start()
                else:
                    write_message(sender, '�� �� ��������� ��������������� !!!')
        elif reseived_message[0:9] == "���������":
            a = open(str(event.user_id) + "c.txt", "w")
            a.write("2")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "�������� ������ ������")
        elif reseived_message[0:11] == "������ qiwi" and i == 2:
                write_message(sender,
                              'Qiwi-������: +79283692011 \n�� �������� ������� ���� ��� � ������������ � �������: ' + "1" + str(sender) + ' ? '
                                            '\n\n����� ������ �� ��� ������ ������������� � ������� ������ ����� ���������� ����� ��������, ���� ������ ������ ��� �������')
        elif reseived_message[0:2] == "��":
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
                    write_message(event.user_id, "������")
                    write_message(str(id), "�� ��� ������ ��������� " + str(bal) + " ���.")
                except:
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                    write_message(event.user_id, "�� �� ������� ���� ��� �����")
            else:
                with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                write_message(sender, '�� �� ��������� ��������������� !!!')
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
                write_message(sender, '������� ������� �����: \n������: 25')
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
                            write_message(str(reseived_message), "��� ������� ������ :)")
                            write_message(str(reseived_message), "�� ��� ������ ��������� " + str(ddd) + " ���.")
                            file = pathlib.Path(str(reseived_message) + "ac.txt")
                            file.unlink()
                            file = pathlib.Path(str(reseived_message) + "aac.txt")
                            file.unlink()
                            file = pathlib.Path(str(reseived_message) + "acc.txt")
                            file.unlink()
                            with open(str(event.user_id) + "c.txt", "r") as ca:
                                i = ca.read()
                                i = int(i)
                            write_message(sender, f'�����: {cdd} \n������: {pas}')
                            write_message(sender, '����������� � �������� :)')
                        else:
                            write_message(sender, '� ��� ������������ ������� !!!')
                    else:
                        write_message(sender, '��.. \n�� ������ ����� ��� ������ !!!')
                        file = pathlib.Path(str(reseived_message) + "ac.txt")
                        file.unlink()
                        file = pathlib.Path(str(reseived_message) + "aac.txt")
                        file.unlink()
                        file = pathlib.Path(str(reseived_message) + "acc.txt")
                        file.unlink()
                        write_message((str(reseived_message)), '� ��� �� ������ ����� ��� ������ !!! \n���������� �� ���� ������ ��� ������� :(')
                except:
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                    write_message(sender, '������� �� ������ :(')
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
                write_message(sender, '������� ������:')
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
                    write_message(sender, f'���������� �� �������� ?\n������: [https://vk.com/id{reseived_message}|{fullname}] ?? \n\n{dd}\n\n����: {ddd} ���.')
                except:
                    write_message(sender, '���������� �� ��������: \n�� ������� :(')
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
                                      f'��� ������� ����������� ? \n��� ���: {sender} \n������ ���������� � �� �����:\nhttps://vk.com/topic-202416186_46921809'
                                      f'\n�� �� �������� �������� ��� ����� � ��� ������ ������ ��� !!!')
                    else:
                        write_message(sender,'�� ������ ����� ��� ������ !!!')
                except:
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(sender, '���-�� ����� �� ��� :( \n���������� ��� ��� !!!')
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
                        write_message(sender, '������� �����:')
                    else:
                        write_message(sender, '����� ������ ���� ������ 0 !!!')
                except:
                    write_message(sender, f'"{reseived_message}" �� �������� ������ !!!')
            else:
                with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                write_message(sender, '� �� �� ����� :/')