from block import Block
import time

class Blockchain():
    def __init__(self):
        self.genesis = self.create_genesis()
        self.head = self.genesis

    def create_genesis(self):
        return Block("Genesis")
    
    def add_block(self, data):
        new_block = Block(data)

        new_block.prev_hash = self.head.hash
        new_block.num = self.head.num + 1

        self.head.next = new_block
        new_block.prev = self.head

        self.head = new_block
    
    def mine(self):
        pass
    
    def print(self):
        temp = self.genesis
        while(temp != None):
            print(temp)
            temp = temp.next

# Test
b = Blockchain()
time.sleep(2)
b.add_block("This is Block 1")
time.sleep(2)
b.add_block("This is Block 2")
time.sleep(2)
b.add_block("This is Block 3")
b.print()