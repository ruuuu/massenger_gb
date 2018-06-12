import time
#from

class MaxLengthField: # для проверки длинного имени

    def __init__(self, name, max_length):
        self.name = name
        self.max_length = max_length

    def __set__(self, instance, value):
        if len(value) > self.max_length:
            raise ToLongError(self.name, value, self.max_length)

        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)



class Jim:

    def to_dict(self):
        return {}

class  JimAction(Jim):

    def __init__(self, action, time):
        self.action = action
        self.time = time


    def to_dict(self):
        result = super().to_dict() # super() - объект класса Jim, вызывается метод бвзового класса
        result['action'] = self.action
        result['time'] = self.time
        return result # возвращает заполненный словарь {'action': 'действие', 'time': 987687906}


class Jim_Message(JimAction):
    to = MaxLengthField('to', 25)
    from_ = MaxLengthField('from', 25)
    message = MaxLengthField('message', 255)

    def __init__(self, to, _from, message, time):
        self.to = to
        self._from = _from
        self.message = message
        self.time = time
        super().__init__('MSG', time) # меняем значеня полей класса JimAction, super() -объект классса JimAction  вызывает свой конструктор

    def proverka(self): # новые значени я полей клсса JimAction
        print('значение поля action класса Jimaction равно', self.action)
        print('значение поля time класса Jimaction равно', self.time)


    def to_dict(self):
        result = super().to_dict() # super() - объект базового класса JimAction
        result['to'] = self.to #"Rufina"
        result['_from'] = self._from # "Николай"
        result['message'] =  self.message #"Привет,Как дела?"
        return result








if __name__ == '__main__':
    j_class = Jim()
    # print('создали путсой словарь', j_class.to_dict())
    #
    message = JimAction('дейсвтие', time.time()) # создаем объект класса JimAction
    # print("поле action равно {}, поле time равно {}".format(message.time, message.action))
    # res_dict = message.to_dict() # вернет заполненный словарь
    # print(" вызов меода to_dict() подкласса дает нам res_dict равysq", res_dict)
    jim_message = Jim_Message("Rufina", "Николай", "Привет,как дела твои?", time.time()) # вызывается консруктор этогоклааса,задем полям значения

    #print('значение поля action ранво {}, значение поля time равно {}'.format(JimAction.action, JimAction.time ))
    jim_message.proverka()
    print('Новый словарь равен', jim_message.to_dict())
    print( 'имеет ди объект класса JimAction поле to', hasattr(message, 'to'))# hasattr(message, 'to') возвращает True, если объект имеет поле
    print('имеет ди объект класса JimAction поле time', hasattr(message, 'time'))
