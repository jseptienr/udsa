def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    Time complexity is O(2LogN) or O(LogN)

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = find_pivot(input_list)
    #print('pivot is {}'.format(pivot))
    if pivot == 0:
        start = 0
        end = len(input_list) - 1
    elif number >= input_list[0]:
        start = 0
        end = pivot
    else:
        start = pivot + 1
        end = len(input_list) - 1

    while start <= end:
        mid = (start + end) // 2
        #print('start is {}, end is {}, mid is {}'.format(start, end, mid))
        if input_list[mid] == number:
            return mid

        if number <= input_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def find_pivot(input_list):
    start = 0
    end = len(input_list) - 1

    if input_list[start] < input_list[end]:
        return 0

    while start <= end:
        mid = (start + end) // 2
        #print('pivot - start is {}, end is {}, mid is {}, elem is {}'.format(start, end, mid, input_list[mid]))
        if input_list[mid] > input_list[mid+1]:
            return mid
        if input_list[mid] > input_list[0]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# additional test cases
test_function([[1, 2, 3, 4, 5, 6], 4]) # non rotated array case
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 7])
test_function([[6, 7, 8, 1, 2, 3, 4], 2])
test_function([[6, 7, 8, 1, 2, 3, 4], 4])
test_function([[6, 7, 8, 1, 2, 3, 4], 6])
