def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    start = 0
    next_0 = 0
    next_2 = len(input_list) - 1
    while start <= next_2:
        if input_list[start] == 0:
            temp = input_list[start]
            input_list[start] = input_list[next_0]
            input_list[next_0] = temp
            start += 1
            next_0 += 1
        elif input_list[start] == 2:
            temp = input_list[start]
            input_list[start] = input_list[next_2]
            input_list[next_2] = temp
            next_2 -= 1
        else:
            start += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

test_function([0, 1, 2])
test_function([2, 1, 0])

test_function([0, 0, 0, 0, 0, 0])
test_function([2, 2, 2, 2])
