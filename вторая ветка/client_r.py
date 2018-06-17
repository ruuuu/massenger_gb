from socket import *
from select import select
import sys

# клиент который пишет

# создаем сокет
# коннект
ADDRESS = ('localhost', 10000)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(ADDRESS)

# он бует читать сообщения
while True:
    msg = sock.recv(1024)
    print(msg.decode('ascii'))