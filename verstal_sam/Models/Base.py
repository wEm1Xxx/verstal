from connection.Connection import *

class Base(Model):
    class Meta:
        database = connect()