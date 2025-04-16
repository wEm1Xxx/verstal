from Models.Good_and_Order import Good_and_Order

class Goods_and_OrderController:
    #Метод вывода всех записей таблицы Статусы
    @classmethod
    def get(cls):
        return Good_and_Order.select()

    @classmethod
    def show(cls, id):
        return Good_and_Order.get_or_none(id)

if __name__ == '__main__':
    for row in Goods_and_OrderController.get():
        print(row.id, row.good_id, row.order_id)