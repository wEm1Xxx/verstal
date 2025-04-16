from unicodedata import decimal

from Models.Base import *

class Goods(Base):
    id = PrimaryKeyField()
    name = CharField()
    cost = DecimalField()
    quantity = DecimalField()
    description = CharField()
    class Meta:
        table_name = 'Goods'

if __name__ == '__main__':
    pass