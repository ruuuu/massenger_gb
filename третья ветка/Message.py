# класс JIM сообщения
from jim.utils import *
from jim.config import *
import time

class  Message:

    def __init__(self):
        pass #  не знаю  какие поля взять для этого класса


    def create_message(self, message_to, text, account_name='Guest'): #{'from': 'Guest', 'message': 'ропопр', 'action': 'msg', 'time': 1528007458.802322, 'to': '#all'}
        return {ACTION: MSG, TIME: time.time(), TO: message_to, FROM: account_name, MESSAGE: text}