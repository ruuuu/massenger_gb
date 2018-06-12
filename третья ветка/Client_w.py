from Response import RResponse # импортирум класс  RResponse  из файла Response.py
import sys
#import logging
#import select
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import send_message, get_message
from jim.config import *
from Message import Message # из файла Message.py импортируем класс Message

class Client_w: # клиент котрый читает

    def __init__(self, login):

        self.client = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
        self.addr = 'localhost'
        self.port = 7777
        self.mode = 'w'
        self.login = login




    def write_messages(self, client):
        """Клиент пишет сообщение в бесконечном цикле"""
        while True:
            # Вводим сообщение с клавиатуры
            text = input('введите сообщение ')
            # Создаем jim сообщение
            m = Message()  # создаем объект калсса Message
            message = m.create_message('#all', text) # вернет словарь {'from': 'Guest', 'message': 'какое-то смс', 'action': 'msg', 'time': 1528007458.802322, 'to': '#all'}
            # отправляем на сервер
            send_message(client, message)

    def read_messages(self, client):
        """
        Клиент читает входящие сообщения в бесконечном цикле
        :param client: сокет клиента
        """
        while True:
            # читаем сообщение
            print('Читаю')
            message = get_message(client)
            print(message)
            # там должно быть сообщение всем
            print(message['message'])

    def client_w(self):

        self.client.connect((self.addr, self.port))
        r = RResponse()

        presence = r.create_presence()  # #  вызываем метод класса Response() , Создаем сообщение для отправки серверу

        send_message(self.client, presence)  # Отсылаем сообщение серверу

        response = get_message(self.client)  # Получаем ответ

        response = r.translate_response(response)  ##  вызываем метод класса Response(), Проверяем ответ полученный от сервера

        if response['response'] == OK:

            if self.mode == 'r':
                self.read_messages(self.client) #  метод же есть в этом же классе
            elif self.mode == 'w':
                self.write_messages(self.client)# метод же есть в этом же классе
            else:
                raise Exception('Не верный режим чтения/записи')


if __name__ == '__main__':
    clt = Client_w('Rufina')# создаем объект класса Client_w
    clt.client_w()# вызов метода класса Client_w