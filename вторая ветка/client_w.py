from socket import *
from select import select
import sys

# клиент который пишет

# создаем сокет
# коннект
ADDRESS = ('localhost', 10000)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(ADDRESS) # сокет клиента

# он бует писать сообщения
while True:
    msg = input('Введите сообщения')
    sock.send(msg.encode('ascii'))


