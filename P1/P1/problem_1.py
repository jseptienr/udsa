class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
            self.tail.next = None
        self.size += 1

    def remove(self, node):
        if node.previous is None:
            self.remove_head()
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
            self.size -= 1

    def remove_head(self):
        if self.head:
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1

    def get_size(self):
        return self.size;

    def __repr__(self):
        l = []
        node = self.head
        while node:
            l.append(str(node.value))
            node = node.next
        l.append('None')
        return "->".join(l)


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.hash_table = {}
        self.dlist = DoublyLinkedList()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.hash_table:
            return -1

        node = self.hash_table[key]
        self.dlist.remove(node)
        self.dlist.append(node)
        return node.value[1]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.hash_table:
            node = self.hash_table[key]
            self.dlist.remove(node)
            self.dlist.append(node)
        elif self.dlist.get_size() < self.capacity:
            node = DoubleNode((key, value))
            self.hash_table[key] = node
            self.dlist.append(node)
        else:
            head = self.dlist.head
            del self.hash_table[head.value[0]]
            self.dlist.remove_head()
            node = DoubleNode((key, value))
            self.hash_table[key] = node
            self.dlist.append(node)


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1
print ("Pass" if our_cache.get(1) == 1 else "Fail")
print ("Pass" if our_cache.get(2) == 2 else "Fail")
print ("Pass" if our_cache.get(3) == -1 else "Fail")
# hat you need is to two data structures really,
#
# a doubly linked list that maintains the ordering, where the nodes hold the values,
# and a hash table (dictionary) that gives you direct access to nodes in the list via keys, so you can get to the values in the nodes in O(1) without traversing the list.
# The operations should do the following:
#
# adding a new key-value pair would add a new node to the end of the list (making the node most recent). The node will hold the value. And you need to add a <key-node reference> entry in the dictionary to find that node later.
# every time you retrieve a value via a key, you use the dictionary to get to the node directly and read its value, then you'll have to move that node from anywhere in the list to the end of the list to make it the most recent.
# whenever you need to add a new key-value pair while the cache is at capacity, you'll have to remove the oldest entry from the list, and remove it's corresponding entry from the dictionary.
