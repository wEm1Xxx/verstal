from Models.Base import *
from Models.User import User
from Models.Status import Status
from Models.Payments import Payments

class Orders(Base):
    id = PrimaryKeyField()
    date = DateTimeField()
    user_id = ForeignKeyField(User)
    status_id = ForeignKeyField(Status)
    payments_id = ForeignKeyField(Payments)
    delivery_data = CharField()
    class Meta:
        table_name = 'Orders'

if __name__ == '__main__':
    pass