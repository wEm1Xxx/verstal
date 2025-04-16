from crypt import methods
from pyexpat.errors import messages
from symbol import return_stmt

from flask import Flask, render_template, request, redirect

from Controllers.GoodsController import GoodsController
from Controllers.UserController import UsersController
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

# создать объект класса Flask
application = Flask(__name__)
application.secret_key = 'la'
# для библиотеки login_manager добавил объект
# этот объект управляет авторизацией
login_manager = LoginManager(application)
@login_manager.user_loader
def user_loader(id):
    return UsersController.show(int(id))
# Маршрут главной страницы
# Добавить методы работы с данными POST и GET

@application.route('/', methods = ['POST', 'GET'])
def home():
    title = "Вход"
    message = ''


    #Проверка метода
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if UsersController.auth(login, password):
            #Создает сессию для пользователя который прошел аутентификацию
            user = UsersController.show_login(login)
            login_user(user)
            print(user)
            print(type(user.role_id))
            if user.role_id.id == 1:
                return redirect('/admin')
            elif user.role_id.id == 2:
                return redirect('/manager')
            else:
                return redirect('/catalog')
        else:
            message = 'Не верный логин или пароль'
    return render_template('login.html',
                           title = title,
                           message = message
                           )

@application.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    title = "Панель администратора"
    if current_user.role_id.id == 1:
        users = UsersController.get()

        if request.method == 'POST':
            login = request.form.get('login')
            role = request.form.get('role_name')

            UsersController.registration(login, 'user1',role)
            return redirect('/admin')

        return render_template('admin.html',
                           title = title, users = users)
    else:
        return redirect('/logout')

@application.route('/manager',methods=['GET', 'POST'])
def manager():
    title = "Панель менеджера"
    if current_user.role_id.id == 2:
        clients=UsersController.get()
        if request.method == 'POST':
            login = request.form.get('login')
            password = request.form.get('password')
            role_id = request.form.get('role_id')
            UsersController.add(login, password, role_id)
            return redirect('/manager')


        return render_template('manager.html',
                            clients=clients,
                            title =title
                           )
    else:
        return redirect('logout')

@application.route('/catalog', methods=['GET', 'POST'])
@login_required
def catalog():
    title = "Каталог товаров"
    if current_user.role_id.id == 3:
        goods = GoodsController.get()

        if request.method == 'POST':
            login = request.form.get('login')
            role = request.form.get('role_name')

            UsersController.registration(login, 'user1',role)
            return redirect('/catalog')

        return render_template('goods.html',
                           title = title, goods = goods)
    else:
        return redirect('/logout')

@application.route('/admin/warehouse', methods=['GET', 'POST'])
@login_required
def warehouse():
    title = 'Складской учёт'
    if current_user.role_id.id == 1:
        return render_template('Warehouse.html', title=title)
    else:
        return redirect('/')

@application.route('/admin/orders', methods=['GET', 'POST'])
@login_required
def orders():
    title = 'История заказов'
    if current_user.role_id.id == 1:
        return render_template('orders.html', title=title)
    else:
        return redirect('/')

@application.route('/admin/users', methods=['GET', 'POST'])
@login_required
def users():
    title = 'Панель управления клиентами'
    
    if current_user.role_id.id == 1:
        return render_template('users.html',users = users, title=title)
    else:
        return redirect('/')

@application.route('/oplata', methods=['GET', 'POST'])
@login_required
def oplata():
    title = 'Оплата товара'
    if current_user.role_id.id == 3:
        return render_template('oplata.html', title=title)
    else:
        return redirect('/')

# выход из системы
@application.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == "__main__":
    application.run(debug=True)