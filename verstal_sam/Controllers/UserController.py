from Models.User import *
from bcrypt import hashpw, gensalt, checkpw

class UsersController:
    #Метод вывода всех записей таблицы Роли
    @classmethod
    def get(cls):
        return User.select()

    @classmethod
    def show(cls, id):
        return User.get_or_none(id)

    @classmethod
    def show_login(cls,login):
        return User.get_or_none(User.login==login)

    @classmethod
    def add(cls, login, password, role_id):
        User.create(login=login,
                     password=password,
                     role_id=role_id)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            User.update({key: value}).where(User.id == id).execute()

    @classmethod
    def delete(cls,id):
        User.delete().where(User.id == id).execute()

    @classmethod
    def registration(cls,login,password,role_id):
        hash_password = hashpw(password.encode('utf-8'),gensalt())
        User.create(login=login,password=hash_password,role_id=role_id)

    #метод проверки логина и пароля - аунтификация
    @classmethod
    def auth(cls,login,password):
        #проверить логин
        if User.get_or_none(User.login == login) != None:
            hspassword = User.get_or_none(User.login == login).password

            # if Users.get_or_none(Users.login == login).password == password:
            if checkpw(password.encode('utf-8'),hspassword.encode('utf-8')):
                return True
        return False

if __name__ == '__main__':
    for row in UsersController.get():
        print(row.id, row.login, row.password, row.role_id)

    UsersController.registration('user3','user3','3')
    #UsersController.registration('gem99', 'F0r3st#Tr3asure', '3')
    #UsersController.registration('pop00', 'Oc3anW@ve_2023', '2')
    #UsersController.registration('joy22', 'N3v3rG1veUp!', '2')
    #UsersController.registration('max33', 'M00nL1ght', '3')
    #UsersController.registration('user2','user2',2)
    #print(UsersController.auth('user1','user1'))