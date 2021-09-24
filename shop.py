from blockchain import Blockchain
from transaction import Transaction

class Shop():
    def __init__(self):
        self.unverified_transactions = []
        self.blockchain = Blockchain()
        self.block_list = []
        self.block_list.append(self.blockchain.genesis.dict())

    def add_transaction(self, customer:str, amount_paid:int, item:str, quantity:int):
        t = Transaction(customer, amount_paid, item, quantity)
        self.unverified_transactions.append(t.dict())

    def mine_transactions(self):
        if (len(self.unverified_transactions) >= 2):
            block_dict = self.blockchain.mine_block(self.unverified_transactions)
            self.block_list.append(block_dict)
            self.unverified_transactions = []
        else:
            print('You need at least 2 transactions to mine a block')

if __name__ == '__main__':

    # Test
    
    s = Shop()

    for i in range(5):
        for j in range(2):
            s.add_transaction('customer', 10, 'item', 6)
        s.mine_transactions()
    s.blockchain.print()