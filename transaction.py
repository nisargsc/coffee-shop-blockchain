import datetime
import json


class Transaction():
    def __init__(self, customer:str, amount_paid:float, item:str, quantity:int):
        self.customer = customer
        self.amount_paid = amount_paid
        self.item = item
        self.quantity = quantity
        self.timestamp = datetime.datetime.now()

    def dict(self):
        transaction_dict = {
            'timestamp' : str(self.timestamp),
            'customer' : self.customer,
            'amount' : self.amount_paid,
            'item' : self.item,
            'quantity' : self.quantity
        }
        return transaction_dict

    def json(self):
        transaction_json = json.dumps(self.dict(), indent=4)
        return transaction_json
        
    def __str__(self):
        return str(self.json())
        # return f"\n \
        # timestamp : {self.timestamp} \n \
        # customer : {self.customer} \n \
        # amount paid (Rs.) : {self.amount_paid} \n \
        # item : {self.item} \n \
        # quantity : {self.quantity} "

if __name__ == '__main__':

    # Test

    t1 = Transaction('a',10,'late10',1)
    t2 = Transaction('b',40,'late20',2)
    t3 = Transaction('c',30,'late10',3)

    print(t1)
    print(t2)
    print(t3)