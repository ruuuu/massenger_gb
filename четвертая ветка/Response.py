
#import sys
#import logging
#import select
import time
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import send_message, get_message
from jim.config import *
from errors import * # из файла errors.py импоритируме все функции



class  RResponse:

    def __init__(self):
        self.message = '' # начальное значение, в методе ему присвоим др значение

    def create_presence(self, account_name="Guest"):  # готовим сообщение для сервера, говорим "Я здесь"

            # if not isinstance(account_name, str):#
            #
            #     raise TypeError# Генерируем ошибку передан неверный тип
            #
            # if len(account_name) > 25:#
            #
            #     raise UsernameToLongError(account_name)# генерируем нашу ошибку имя пользователя слишком длинное

            self.message = {    # формируем словарь сообщения для сервера
                'action': 'presence', #PRESENCE,
                'time': time.time(),
                'user': {
                    'account_name': account_name
                }
            }

            return self.message

    def translate_response(self, response):  # Словарь -ответ от сервера
        """
        Разбор сообщения
        :param response: Словарь ответа от сервера
        :return: корректный словарь ответа
        """

        # if not isinstance(response, dict):  # Передали не словарь
        #     raise TypeError
        #
        # if RESPONSE not in response:  # Нету ключа response
        #     raise MandatoryKeyError(RESPONSE)  # Ошибка нужен обязательный ключ


        code = response['response']  # получаем код ответа RESPONSE

        # if len(str(code)) != 3:  # длина кода не 3 символа
        #     raise ResponseCodeLenError(code)  # Ошибка неверная длина кода ошибки
        #
        # if code not in RESPONSE_CODES:# неправильные коды символов
        #    raise ResponseCodeError(code) # ошибка неверный код ответа

        return response# возвращаем ответ