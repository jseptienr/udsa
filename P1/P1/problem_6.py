class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    new_list = LinkedList()
    node = llist_1.head
    unique_values = set()
    while node:
        val = node.value
        if val not in unique_values:
            new_list.append(node.value)
            unique_values.add(node.value)
        node = node.next
    node = llist_2.head
    while node:
        val = node.value
        if val not in unique_values:
            new_list.append(node.value)
            unique_values.add(node.value)
        node = node.next
    return new_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    new_list = LinkedList()
    node = llist_1.head
    unique_values = set()
    while node:
        unique_values.add(node.value)
        node = node.next
    node = llist_2.head
    existing_values = set()
    while node:
        if node.value in unique_values and node.value not in existing_values:
            new_list.append(node.value)
            existing_values.add(node.value)
        node = node.next
    return new_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('Test 1')
print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print('Test 2')
print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3: equal lists union and intersection are the same

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65]
element_2 = [3,2,4,35,6,65]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print('Test 3')
print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
