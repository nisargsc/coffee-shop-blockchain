import hashlib
import datetime


class Block():
    def __init__(self, data):
        self.num = 0
        self.nonce = 0
        self.data = data
        self.prev_hash = 0X0
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
    
    def check_validity(self):
        print(self.hash)
        print(self.find_hash())
        return (int(self.hash,base=16) == int(self.find_hash(),base=16))
           
    def __str__(self):
        return f" \
        num : {self.num} \n \
        timestamp : {self.timestamp} \n \
        data : {self.data} \n \
        prev_hash : {self.prev_hash} \n \
        hash : {self.hash} \n \
        nonce : {self.nonce} \n"


# # Test
# block = Block("genesis")
# print(block)
# print(block.check_validity())

# # altering the data and checking the validity
# block.data = "Genesis"
# print(block)
# print(block.check_validity())

# # checking the validity after updating the hash
# block.update_hash()
# print(block)
# print(block.check_validity())