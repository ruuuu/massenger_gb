# класс JIM сообщения
from jim.utils import *
from jim.config import *
import time

class  Message:

    def __init__(self):
        pass #

    #создаем сообщение тому, кто читает
    def create_message(self, message_to, text, account_name='Rufina'): #{'from': 'Guest', 'message': 'ропопр', 'action': 'msg', 'time': 1528007458.802322, 'to': '#all'}
        return {'action': MSG, 'time': time.time(), 'to': message_to, 'from': account_name, 'message': text}