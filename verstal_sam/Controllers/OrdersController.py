from datetime import datetime, timedelta
from itertools import count
from Models.Orders import *
from peewee import *
import calendar


class OrdersController:

    @classmethod
    def get(cls):
        return Orders.select()

    @classmethod
    def show(cls, id):
        return Orders.get_or_none(id)

    @classmethod
    def add(cls,date, user_id, status_id, payments_id, delivery_data):
        Orders.create(date=date,
                      user_id=user_id,
                      status_id=status_id,
                      payments_id=payments_id,
                      delivery_data=delivery_data)


    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Orders.update({key: value}).where(Orders.id == id).execute()

    @classmethod
    def count(cls):
        count = Orders.select().count()
        return count

    @classmethod
    def report_range(cls,day):

        given_day = datetime.strptime(day, '%Y-%m-%d')
        start_of_week = given_day - timedelta(days=given_day.weekday())

        # Создаем список дней недели
        week_days = [start_of_week + timedelta(days=i) for i in range(7)] #Однострочная конструкция цикла
        count = Orders.select().where((Orders.date >= start_of_week) & (Orders.date <= week_days[6])).count()
        return count

    @classmethod
    def report_day(cls,day):
        return Orders.select().where(Orders.date == day).count()

    @classmethod
    #метод вывода отчёта в случайном периоде
    def report_random(cls, day1, day2):
        return Orders.select().where(Orders.date.between(day1,day2)).count()

    @classmethod
    def get_orders_in_month(cls, start_date, end_date):
        # last_day = calendar.monthrange(year, month)
        # start_date = datetime(year, month, 1)
        # end_date = datetime(year, month, last_day)
        # return Orders.select().where((Orders.date >= start_date) & (Orders.date <= end_date))
        # Преобразуем строку в дату
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # Теперь можно сравнивать
        count = Orders.select().where(
            (Orders.date >= start_date) & (Orders.date <= end_date)
        ).count()
        return count


if __name__ == '__main__':

   # for row in OrdersController.get():
    #    print(row.id, row.date, row.user_id, row.status_id, row.payments_id, row.delivery_data)
    #print('--------------------------------------')
    #OrdersController.add('2012-12-12','10','2','1','2012-12-12')
    #print(OrdersController.count())
   #OrdersController.report('2025-03-06')
   #OrdersController.report('2024-05-12')
   #print(OrdersController.report_range('2023-07-22'))
   #print(OrdersController.report_day('2023-07-22'))
   #print(OrdersController.report_random('2023-07-22','2023-10-20'))
    #print(OrdersController.get_orders_between_dates('2023-07-22','2023-10-20'))
    print(OrdersController.get_orders_in_month('2023-07-01','2023-07-31'))


