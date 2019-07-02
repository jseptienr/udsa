import sys
import heapq

class TreeNode:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __lt__(self, other):
        return self.freq <= other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __str__(self):
        return '({}, {})'.format(self.value, self.freq)

    def __repr__(self):
        return '({}, {})'.format(self.value, self.freq)


def calculate_frequency(data):
    d = dict()
    for val in data:
        if val not in d:
            d[val] = 1
        else:
            d[val] += 1
    l = []
    for val, freq in d.items():
        l.append(TreeNode(val, freq))
    return l


def encode(root, code, values):
    if not root:
        return

    if root.left is None and root.right is None:
        if code is '':
            values[root.value] = '1'
        else:
            values[root.value] = code

    encode(root.left, code+'0', values)
    encode(root.right, code+'1', values)


def huffman_encoding(data):
    if len(data) == 0:
        return None, None

    que = calculate_frequency(data)
    heapq.heapify(que)
    while len(que) > 1:
        n1 = heapq.heappop(que)
        n2 = heapq.heappop(que)
        n3 = TreeNode('\0', n1.freq+n2.freq)
        n3.left = n1
        n3.right = n2
        heapq.heappush(que, n3)
    values = dict()
    root = heapq.heappop(que)
    encode(root, '', values)
    encoded_data = []
    for c in data:
        encoded_data.append(values[c])
    return ''.join(encoded_data), root


def huffman_decoding(data,tree):
    if not data:
        return ''

    result = []
    index = 0
    root = tree
    for bit in data:
        if root.left and bit == '0':
            root = root.left
        elif root.right and bit == '1':
            root = root.right
        if root.left is None and root.right is None:
            result.append(root.value)
            root = tree
    # if root and (root.left is None or root.right is None):
    #     result.append(root.value)
    return ''.join(result)


if __name__ == "__main__":
    # print('TEST 1')
    a_great_sentence = "The bird is the word"

    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))

    print('Pass' if a_great_sentence == decoded_data else 'Fail')

    # TEST 2: odd
    # print('TEST 2')

    a_great_sentence = "The birds are the words"

    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))

    print('Pass' if a_great_sentence == decoded_data else 'Fail')

    # TEST 3: single character
    # print('TEST 3')
    a_great_sentence = 'r'

    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))

    print('Pass' if a_great_sentence == decoded_data else 'Fail')

    # TEST 4: short even
    # print('TEST 4')
    a_great_sentence = "op"
    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))

    print('Pass' if a_great_sentence == decoded_data else 'Fail')

    # TEST 5: long
    # print('TEST 5')
    a_great_sentence = "Like an expensive sports car, fine tuned and well built, Portia was sleek, shapely, and gorgeous, her red jumpsuit molding her body, which was as warm as the seatcovers in July, her hair as dark as new tires, her eyes flashing like bright hubcaps, and her lips as dewy as the beads of fresh rain on the hood; she was a woman driven—fueled by a single accelerant—and she needed a man, a man who wouldn't shift from his views, a man to steer her along the right road, a man like Alf Romeo."
    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))

    print('Pass' if a_great_sentence == decoded_data else 'Fail')

    # TEST 6: empty string
    # print('TEST 5')
    a_great_sentence = ""
    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))

    print('Pass' if a_great_sentence == decoded_data else 'Fail')

    # TEST 7: repeated char
    # print('TEST 5')
    a_great_sentence = "AAAAAAAAA"
    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))

    print('Pass' if a_great_sentence == decoded_data else 'Fail')
