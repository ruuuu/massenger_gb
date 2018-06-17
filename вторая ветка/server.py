import select
from socket import socket, AF_INET, SOCK_STREAM
#from  03_sockets.echo_server_select_to_dz import read_requests

# создать сокет, повешать на адрес
address = ('', 10000)
s = socket(AF_INET, SOCK_STREAM)
s.bind(address)
s.listen(100)
# ставим таймаут для переключения с accept
s.settimeout(0.2)   # Таймаут для операций с сокетом

# у нас будет много клиентов
clients = []

# в цикле обрабатываем клиентов
while True:
    # ждем подключения
    conn, addr = s.accept() # клиент подключается к серверу
    # сохраняем клиента в список
    clients.append(conn) # подключенного клиента добавляем   в список
    # начинаем мониторить что нужно сделать
    # кто нам пишет и кто читает
    who_writes, who_reads, e = select.select(clients, clients, clients, 0)# who_writes - клиенты  котрые отправляют запрос на сервер
                                                                          # who_reads -клинты котрые принмиают ответ  от сервера

    responses = {}  # Словарь запросов клиентов, вида {сокет: запрос} , заполняем его в  цикле ниже
    for who_write in who_writes:  # для каждого клента  который отправил запрос на сервер
        # что  написали
        data = who_write.recv(1024).decode('ascii')  # этот клмент принимает сообщение(ответ) data от сервера
        responses[who_write] = data  # клиенту с сокетом who_write сервер отвечает сообщением data

        print(who_write)

    for who_read in who_reads: # для кажддго клиента,который принимает ответ от сервера
        # Подготовить и отправить ответ сервера
        resp = responses[who_read].encode('ascii') # ответ resp для этого клиента who_read
        test_len = who_read.send(resp) # клиент  who_read получате ответ  от сервера

        print(who_read)
