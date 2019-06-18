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

# def sort(que):
#     return sorted(que, key=lambda kv: kv[1])

def get_code(tree):
    if tree.right or tree.
def huffman_encoding(data):
    que = calculate_frequency(data)
    #print(que)
    heapq.heapify(que)
    #print(que)
    while len(que) > 1:
        n1 = heapq.heappop(que)
        n2 = heapq.heappop(que)
        n3 = TreeNode('\0', n1.freq+n2.freq)
        n3.left = n1
        n3.right = n2
        heapq.heappush(que, n3)

    for c in data:
        get_code(tree)
        #print(que)
    #print(que[0])
    # e1 = que.pop(0)
    # e2 = que.pop(0)
    # n1 = TreeNode(e1[0], e1[1])
    # n2 = TreeNode(e2[0], e2[1])
    # n3 = TreeNode('\0', n1.val+n2.val)
    # que.append(('\0', e1[1] + e2[1]))
    # que.sort(key=lambda tup: tup[1])
    # print(que)



def huffman_decoding(data,tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    huffman_encoding(a_great_sentence)

    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))
    #
    # encoded_data, tree = huffman_encoding(a_great_sentence)
    #
    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))
    #
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))
