from Models.Base import *

class Payments(Base):
    id = PrimaryKeyField()
    summ = DecimalField()
    date = DateTimeField()
    class Meta:
        table_name = 'Payments'

if __name__ == '__main__':
    pass