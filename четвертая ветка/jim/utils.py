import json




def dict_to_bytes(message_dict):
    """
    Преобразование словаря в байты
    :param message_dict: словарь
    :return: bytes
    """
    # Проверям, что пришел словарь
    if isinstance(message_dict, dict):

        jmessage = json.dumps(message_dict)# Преобразуем словарь в json

        bmessage = jmessage.encode('utf-8')# Переводим json в байты

        return bmessage# Возвращаем байты
    else:
        raise TypeError


def bytes_to_dict(message_bytes):
    """
    Получение словаря из байтов
    :param message_bytes: сообщение в виде байтов
    :return: словарь сообщения
    """
    # Если переданы байты
    if isinstance(message_bytes, bytes):

        jmessage = message_bytes.decode('utf-8') # Декодируем

        message = json.loads(jmessage)# Из json делаем словарь

        if isinstance(message, dict):# Если там был словарь

            return message#  словарь
        else:

            raise TypeError
    else:

        raise TypeError


def send_message(sock, message):
    """
    Отправка сообщения
    :param sock: сокет
    :param message: словарь сообщения
    :return: None
    """

    bprescence = dict_to_bytes(message)# Словарь переводим в байты

    sock.send(bprescence) # Отправляем


def get_message(sock):
    """
    Получение сообщения
    :param sock:
    :return: словарь ответа
    """

    bresponse = sock.recv(1024)# Получаем байты

    response = bytes_to_dict(bresponse) # переводим байты в словарь

    return response# словарь
