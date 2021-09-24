import hashlib
from block import Block

class Blockchain():
    def __init__(self):
        self.difficulty = 4
        self.genesis = None
        self.create_genesis()
        self.head = self.genesis

    def create_genesis(self):
        self.genesis = Block(0, "Genesis")
        self.proof_of_work(self.genesis)
    
    def mine_block(self, data):
        num = self.head.num + 1
        prev_hash = self.head.hash
        new_block = Block(num, data, prev_hash)

        
        new_block.prev = self.head
        self.proof_of_work(new_block)
        self.head.next = new_block

        self.head = new_block

        return new_block.dict()
    
    def proof_of_work(self, block:Block):
        while self.valid_proof(block) is False:
            block.nonce += 1
        block.update_hash()
        
    
    def find_guess_hash(self, block:Block):
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
        return self.find_guess_hash(block)[:self.difficulty]=="0" * self.difficulty
    
    def print(self):
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