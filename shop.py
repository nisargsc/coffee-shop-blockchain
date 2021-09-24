from blockchain import Blockchain
from transaction import Transaction

class Shop():
    """
    Class for the coffee shop

    :attr unverified_transactions: <list> Array of all the unverified transactions yet to be mined
    :attr blockchain: <Blockchain> Blockchian with block data as list of varified transactions
    :attr block_list: <list> Array for the blockchain. with block_dict as elements

    :method add_transaction(): Adds new transactions to unverified_transactions list
    :method mine_transactions(): Mines all the transactions from the unverified_transactions list into a block
    """
    def __init__(self):
        """
        :return: None
        """
        self.unverified_transactions = []
        self.blockchain = Blockchain()
        self.block_list = []
        self.block_list.append(self.blockchain.genesis.dict())

    def add_transaction(self, customer:str, amount_paid:float, item:str, quantity:int):
        """
        Adds new transactions to unverified_transactions list

        :param customer: <str> Name of the customer
        :param amount_paid: <float> Amount paid by the customer
        :param item: <str> Name of the item ordered by the customer
        :param quantity: <int> Quantity of the item ordered by the customer

        :return: None
        """
        t = Transaction(customer, amount_paid, item, quantity)
        self.unverified_transactions.append(t.dict())

    def mine_transactions(self):
        """
        Mines all the transactions from the unverified_transactions list into a block and resets the list

        :return: None
        """
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