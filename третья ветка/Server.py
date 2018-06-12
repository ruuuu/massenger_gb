import sys
import logging
import select
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import send_message, get_message
from jim.config import *


class Server:

    def __init__(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.addr = ''
        self.port= 7777
        self.server.bind((self.addr, self.port))  # Присваивает порт 7777
        self.server.listen(15)
        # Не забываем поставить таймаут иначен ничего не случиться
        self.server.settimeout(0.2)
        self.clients = []

    def presence_response(self, presence_message):  # передаем presence_message-сообщение клиента {ACTION:PRESENCE, TIME:time.time()}, сервер посылает сообщение-словарь клиенту
        # # Делаем проверки
        if 'action' in presence_message and \
                presence_message['action'] == 'presence' and \
                'time' in presence_message and \
                isinstance(presence_message['time'], float):
                return {'response': 200}# Если всё хорошо шлем ОК {RESPONSE: 200}
        else:
                return {'response': 400, 'error': 'Не верный запрос'} # Шлем код ошибки

        return {'response': 200}  # Если всё хорошо шлем ОК {RESPONSE: 200}

    def read_requests(self, r_clients, all_clients):  # r_clients: клиенты которые могут отправлять сообщения
        # Список входящих сообщений то есть список словарей
        messages = []  # в цикле заполняем

        for sock in r_clients:  # для каждого клиента котрый читает
            try:
                # Получаем входящие сообщения
                # message словарь(сообщение), переведенный из байтов
                message = get_message(sock)  # передаем сокет клиента котрый читает

                # В идеале нам нужно сделать еще проверку, что сообщение нужного формата прежде чем его пересылать!
                # Пока оставим как есть, этим займемся позже
                messages.append(message)  # Добавляем входящие сообщение(кторое клиент-sock прочитал) в список
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                all_clients.remove(sock)  # удаляем его из всех клиентов

        # Возвращаем список словарей( сообщений) [{словарь 1},{словарь2},{словарь3},{словарь4}]
        return messages

    def write_responses(self, messages, w_clients, all_clients):
        """
        Отправка сообщений тем клиентам, которые их ждут
        :param messages: список сообщений(словарей)
        :param w_clients: клиенты которые читают
        :param all_clients: все клиенты
        :return:
        """

        for sock in w_clients:
            # Будем отправлять каждое сообщение всем
            for message in messages:
                try:
                    # Отправить на тот сокет, который ожидает отправки
                    # print('Заходит')
                    send_message(sock, message)
                except:  # Сокет недоступен, клиент отключился
                    print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                    sock.close()
                    all_clients.remove(sock)




    def server_main(self):

        while True:
             try:
                 conn, addr = self.server.accept()  # клиент подключается, получаем сокет подключенного клиента П

                 presence = get_message(conn)  # получаем сообщение presence(словарь) от клиента с сокетом conn

                 response = self.presence_response(presence)  # почему ругается? метод же в этом же классе ,   формируем ответ этому клиенту, response  - словарь {ACTION:PRESENCE, TIME:time.time()}

                 send_message(conn, response)  # отправляем ответ - response клиенту conn
             except OSError as e:
                  pass  # timeout вышел
                  #print('ошибка таймаута', e)
             else:
                 print("Получен запрос на соединение от %s" % str(addr))  # выводим адре  клиента,котрый подклчился
                 self.clients.append(conn)

             finally:
                 # Проверить наличие событий ввода-вывода
                 wait = 0
                 r = []
                 w = []
                 try:
                     r, w, e = select.select(self.clients, self.clients, [], wait)  # w-клиенты, котроые читают, r-клиент котрые отправляют
                 except:
                     pass  # Ничего не делать, если какой-то клиент отключился

                 # клиентв из r пишут сообщения
                 requests = self.read_requests(r, self.clients)  #  Получаем  список-requests входных сообщений(список словарей) от клиента
                 self.write_responses(requests, w, self.clients)  #   Выполним отправку  списока входящих сообщений(словарей) клиентам котрые читают


if __name__ == '__main__':
    s = Server()
    s.server_main()