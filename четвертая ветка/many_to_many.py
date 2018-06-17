# сдалеть бд для хранения контактов
# гланые таблицы клинет, контакты
# сделать и проверить отедельно (тесты, скрипт)


from sqlalchemy.ext.declarative import \
    declarative_base  # Для использования декларативного стиля необходима функция declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, \
    ForeignKey  # Импортируем необходимые классы (типы данных, таблицы, метаданные, ключи)
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

# Проверим версию SQLAlchemy
try:
    import sqlalchemy

    print(sqlalchemy.__version__)
except ImportError:
    print('Библиотека SQLAlchemy не найдена')
    sys.exit(13)

# Создадим БД в памяти или в файле
# engine-движок создаем:
engine = create_engine('sqlite:///mydb.sqlite',
                       echo=True)  ## Флаг `echo` включает ведение лога через стандартный модуль `logging` Питона.
Session = sessionmaker(bind=engine)  # ерез эту штуку ьудет соединение с бд
Base = declarative_base()  # Функция declarative_base создаёт базовый класс для декларативной работы

# создаем таблицу-связку 'Users_ClientContact':  много-ко многим 'Users'-'ClientContact'
# association_table = Table('Users_ClientContact', Base.metadata, Column('user_id', Integer, ForeignKey('Users.id')),
#                           Column('contact_id', Integer, ForeignKey('ClientContact.ContactId')))
#

# Декларативное создание таблицы и класса :

# клиент
class Users(Base):  # первичный класс
    __tablename__ = 'Users'  # создаю тпблицу 'Users'
    id = Column(Integer, primary_key=True)  # обращаемся к полю как User.id , User.name
    name = Column(String, unique=True)

    #

    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     return "User('%s')" % (self.name)


class ClientContact(Base):  # конаткты клиентов ?дочерний класс
    __tablename__ = 'ClientContact'  # создаю тпблицу 'ClientContact'
    id = Column(Integer, primary_key=True)
    ClientId = Column(Integer, ForeignKey('Users.id'))
    ContactId = Column(Integer, ForeignKey('Users.id'))

    def __init__(self, ClientId, ContactId):
        self.ClientId = ClientId
        self.ContactId = ContactId


Base.metadata.create_all(engine)  # в бд создаются таблицы

# Таблица 'users' доступна через атрибут класса Users
users_table = Users.__table__
print('Declarative. Table:', users_table)  # вывдет название таблицы

Session.configure(bind=engine)

session = Session()  # Класс Session будет создавать Session-объекты, которые привязаны к базе данных

# #добавление данных в таблицу 'Users':
user_1 = Users('Rufina')
user_2 = Users('Irina')
user_3 = Users('Lilia')

#session.add(user_1)

#session.add_all([user_2, user_3])

user_4 = Users('Olga')
user_5 = Users('Oleg')
#session.add_all([user_4, user_5])# добавим еще одну запись в таблицу Users





# # заполняем таблицу 'ClientContact':
contact_1 = ClientContact(1, 2)
contact_2 = ClientContact(1, 3)
contact_3 = ClientContact(2, 3)
#
#session.add_all([contact_1,contact_2,contact_3])# сразу все три записи добавляем





#
q_user = session.query(Users).filter_by(name="Rufina")
print("первый запрос", q_user[0].name) #('Rufina', 1, 0)

q_userr = session.query(Users).all()
print(type(q_userr))
print("Таблица Users:")
for i in range(5): # выводим таблицу Users
     print(q_userr[i].id, '|', q_userr[i].name)

#print(q_userr[3].name)

qq_user = session.query(Users).all()
print('simple', qq_user)

q_clcomtact = session.query(ClientContact).all()
print(type(q_clcomtact))
print("Таблица ClientContact:")
for i in range(3): # выводим таблицу Users
     print(q_clcomtact[i].ClientId,  q_clcomtact[i].ContactId)



# 2 часть дз, сделать запросы: список контактов, добавление, удаление, изменение

# Добавление новых объектов, то есть  записей в таблицу Users:
user_6 = Users("vasia")
#session.add(user_6) # добавляем запиьс в таблицу нашу

user_6.name = 'Zina' # меняем имя c "vasia" на 'Zina'
print('поменяли  строку, была vasia, стала ' ,user_6.name)

print('Добавлем новую запись в таблицу Users:')
main_user = Users('Alex')# создали новую запись
#session.add(main_user)# добавляем ее в бд

print(main_user.name)
#session.commit()
#print( main_user.id, main_user.name)

#session.delete(main_user) # удаляем запись
session.commit()  # сохранем данные в бд

#session.rollback()
session.close()