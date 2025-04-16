from Models.Payments import *

class PaymentsController:
    @classmethod
    def get(cls):
        return Payments.select()

    @classmethod
    def show(cls, id):
        return Payments.get_or_none(id)


if __name__ == '__main__':
    for row in PaymentsController.get():
        print(row.id, row.summ, row.date)