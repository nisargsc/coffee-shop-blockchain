import hashlib
import datetime
import json

class Block():
    def __init__(self, num:int, data:str, prev_hash=None):
        self.num = num
        self.nonce = 0
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.find_hash()
        self.next = None
        self.prev = None
        self.timestamp = datetime.datetime.now()

    def find_hash(self):
        hash = hashlib.sha256()
        block_string = f"{self.num}{self.data}{self.prev_hash}{self.nonce}"
        hash.update(block_string.encode('utf-8'))
        return hash.hexdigest()

    def update_hash(self):
        self.hash = self.find_hash() 

    def dict(self):
           block_dict = {
               'num' : self.num,
               'timestamp' : str(self.timestamp),
               'data' : self.data,
               'prev_hash' : self.prev_hash,
               'hash' : self.hash,
               'nonce' : self.nonce
           }
           return block_dict

    def __str__(self):
        return str(json.dumps(self.dict(), indent = 4))
        # return f"\n \
        # num : {self.num} \n \
        # timestamp : {self.timestamp} \n \
        # data : {self.data} \n \
        # prev_hash : {self.prev_hash} \n \
        # hash : {self.hash} \n \
        # nonce : {self.nonce} \n \"

if __name__ == '__main__':

    # Test

    block = Block(0,"genesis")
    print(block)

    block.data = "Genesis"
    block.update_hash()
    print(block)