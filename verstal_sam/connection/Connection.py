from peewee import *
#функция подключения к БД
def connect():
    mysql_db = MySQLDatabase('GevS1234_site',
                             user='GevS1234_1212',
                             password='123123',
                             host='10.11.13.118',
                             port=3306)
    return mysql_db

if __name__ == "__main__":
    connect().connect()