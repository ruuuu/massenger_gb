from Response import RResponse # импортирум класс  Response  из файла response.py
from Message import Message # из файла Message.py импортируем класс Message
import sys
import logging
import select
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import send_message, get_message
from jim.config import *

class Client_r: # клиент котрый отправляет

    def __init__(self):

        self.client = socket(AF_INET, SOCK_STREAM)  # клиент, котрый отправляет
        self.addr = 'localhost'
        self.port = 7777
        self.mode = 'r'



    # def write_messages(self, client):
    #     """Клиент пишет сообщение в бесконечном цикле"""
    #     while True:
    #         # Вводим сообщение с клавиатуры
    #         text = input(':)>')
    #         # Создаем jim сообщение
    #         m = Message() # создаем объект калсса Message
    #         message = m.create_message('#all', text)
    #         # отправляем на сервер
    #         send_message(client, message)

    def read_messages(self, client): # клиент котрый отправляет
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
            print(message[MESSAGE])



    def client_r(self):
        self.client.connect((self.addr, self.port))
        r = RResponse()
        presence = r.create_presence()  #  вызываем метод класса Response(), Создаем сообщение для отправки серверу
        send_message(self.client, presence)  # Отсылаем сообщение серверу
        response = get_message(self.client)  # Получаем ответ от сервера
        response = r.translate_response(response)  # вызываем метод класса Response(), Проверяем ответ полученный от сервера
        if response['response'] == OK:
            # в зависимости от режима мы будем или слушать или отправлять сообщения
            if self.mode == 'r':
                self.read_messages(self.client)# вызов метода этого класса
            # elif self.mode == 'w':
            #     self.write_messages(self.client)# вызов метода этого класса
            # else:
            #     raise Exception('Не верный режим чтения/записи')


if __name__ == '__main__':
    clt = Client_r() # создаем объект класса Client_r
    clt.client_r()# вызов метода класса Client_r