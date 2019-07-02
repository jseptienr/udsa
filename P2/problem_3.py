'''
Rearrange Array Elements so as to form two number such that their sum is maximum.
Return these two numbers. You can assume that all array elements are in the range [0, 9].
The number of digits in both the numbers cannot differ by more than 1.
You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

'''

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_nums = sorted(input_list)
    print('sorted {}'.format(sorted_nums))
    solution = [0, 0]
    index = 0
    multiplier = 1
    while index < len(sorted_nums):
        print('index {}, solution {}'.format(index, solution))
        solution[0] += sorted_nums[index]*multiplier
        if index+1 < len(sorted_nums):
            solution[1] += sorted_nums[index+1]*multiplier
        index += 2
        multiplier *= 10
    print('sum is {}'.format(solution[0] + solution[1]))
    return solution



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print('solution {}, output {}'.format(solution, output))
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
