import hashlib
from block import Block

class Blockchain():
    """
    Class for the blockchain

    :attr difficulty: <int> Difficulty level for mining neew block
    :attr genesis: <Block> First block of the blockchain
    :attr head: <Block> Latest block in the blockchain

    :method create_genesis(): Creates the genesis block
    :method mine_block(): Mines new block in the blockchain
    :method proof_of_work(): Updates the nonce and hash of the block according to the proof of work algoritm
    :method find_guess_hash(): Finds hash for the guesss to be used in proof of work algoritm
    :method valid_proof(): Checks if the block has valid proof or not
    :method print(): Prints the blockchain
    """

    def __init__(self):
        """
        :return: None
        """
        self.difficulty = 4
        self.genesis = None
        self.create_genesis()
        self.head = self.genesis

    def create_genesis(self):
        """
        Creates the genesis block

        :return: None
        """
        self.genesis = Block(0, "Genesis")
        self.proof_of_work(self.genesis)
    
    def mine_block(self, data):
        """
        Mines new block

        :param data: <any> Data to store in the block. Can be of any type.

        :return: <dict> dict with the details of the block mined
        """
        # Creating new block
        num = self.head.num + 1
        prev_hash = self.head.hash
        new_block = Block(num, data, prev_hash)

        # Seting the linked-list pointers and applying proof_of_work()
        new_block.prev = self.head
        self.proof_of_work(new_block)
        self.head.next = new_block

        self.head = new_block

        return new_block.dict()
    
    def proof_of_work(self, block:Block):
        """
        Updates the nonce and the hash of the block according to the proof of work algoritm

        :param block: <Block>

        :return: None
        """
        while self.valid_proof(block) is False:
            block.nonce += 1
        block.update_hash()
        
    
    def find_guess_hash(self, block:Block):
        """
        Finds hash for the guesss to be used in proof of work algoritm

        :param block: <Block>
        :return: <str> hash for the guess using prev_nonce, prev_hash, and nonce
        """
        if (self.genesis == None or self.genesis == block):
            guess = f"0g3N3s1Sbl0ck{block.nonce}".encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
        else:
            prev_nonce = block.prev.nonce
            prev_hash = block.prev.hash
            guess = f"{prev_nonce}{prev_hash}{block.nonce}".encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash

    def valid_proof(self, block:Block):
        """
        Validates the proof according to the proof of work algoritm

        :param block: <Block>

        :return: <bool> True if guess_hash has its fist 'self.difficulty' digits as '0'.
        """
        return self.find_guess_hash(block)[:self.difficulty]=="0" * self.difficulty
    
    def print(self):
        """
        Prints the blockchain

        :return: None
        """
        temp = self.genesis
        while(temp != None):
            print(temp)
            temp = temp.next

if __name__ == '__main__':

    # Test

    b = Blockchain()

    print(b.head)
    for i in range(10):
        b.mine_block("This is Block " + str(i))
        print(b.head)