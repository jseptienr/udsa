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
        self.head = None

    def add_block(self, data):
        timestamp = datetime.datetime.now(datetime.timezone.utc)

        if not self.head:
            self.head = Node(Block(timestamp, data, '0'))
        else:
            node = Node(Block(timestamp, data, self.head.value.hash))
            curr = self.head
            node.next = curr
            self.head = node

    def print_blockchain(self):
        print(self)

    def __str__(self):
        node = self.head
        l = list()
        while node:
             l.append(str(node.value))
             node = node.next
        return '\n'.join(l)


blockchain = Blockchain()
blockchain.add_block('test')
blockchain.add_block('test2')
blockchain.add_block('test3')
blockchain.add_block('test4')
blockchain.add_block('test5')
print(blockchain)
blockchain.print_blockchain()
