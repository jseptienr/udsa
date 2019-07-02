import hashlib
import datetime


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev_block = None

    def calc_hash(self):
          sha = hashlib.sha256()

          sha.update(self.timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%Z").encode('utf-8'))
          sha.update(self.data.encode('utf-8'))
          sha.update(self.previous_hash.encode('utf-8'))

          return sha.hexdigest()

    def __str__(self):
        return '[\n timestamp: {},\n data: {},\n hash: {},\n prev_hash: {}\n]'.format(self.timestamp,
                                                                            self.data,
                                                                            self.hash,
                                                                            self.previous_hash)


class Blockchain:
    def __init__(self):
        self.latest_block = None
        self.size = 0

    def add_block(self, data):
        timestamp = datetime.datetime.now(datetime.timezone.utc)
        self.size += 1
        if not self.latest_block:
            self.latest_block = Block(timestamp, data, '0')
        else:
            block = Block(timestamp, data, self.latest_block.hash)
            curr = self.latest_block
            block.prev_block = curr
            self.latest_block = block

    def print_blockchain(self):
        print(self)

    def __len__(self):
        return self.size

    def __str__(self):
        if self.size == 0:
            return 'Empty Blockchain'

        block = self.latest_block
        l = list()
        while block:
             l.append(str(block))
             block = block.prev_block
        return '\n'.join(l)


blockchain = Blockchain()

print('pass' if str(blockchain) == 'Empty Blockchain' else 'fail')

blockchain.add_block('test')
print('pass' if blockchain.latest_block.previous_hash == '0' else 'fail')

blockchain.add_block('test2')
blockchain.add_block('test3')
print('pass' if blockchain.latest_block.previous_hash != '0' else 'fail')

blockchain.add_block('test4')
blockchain.add_block('test5')
print('pass' if len(blockchain) == 5 else 'fail')

curr_hash = blockchain.latest_block.hash
blockchain.add_block('test6')
print('pass' if blockchain.latest_block.previous_hash == curr_hash else 'fail')

#print(blockchain)
