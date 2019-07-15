def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = ints[0]
    max = ints[0]
    for i in ints:
       if i < min:
           min = i
       if i > max:
           max = i
    return (min, max)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(10, 100)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((10, 99) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 1000)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 999) == get_min_max(l)) else "Fail")
