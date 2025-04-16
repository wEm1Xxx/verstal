from Models.Base import *
from Models.Goods import Goods
from Models.Orders import Orders

class Good_and_Order(Base):
    id = PrimaryKeyField()
    good_id = ForeignKeyField(Goods)
    order_id = ForeignKeyField(Orders)

    class Meta:
        table_name = 'Good_and_Order'

if __name__ == '__main__':
    pass