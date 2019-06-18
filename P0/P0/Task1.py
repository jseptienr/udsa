"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

def updateSet(unique_nums, count, num):
    """Converts a set of telephone records and returns a single lsit.
    Inputs: list of records with two phone numbers in index 0 and 1
    Output: single list of records
    """
    if num not in unique_nums:
        unique_nums.add(num)
        count += 1
    return unique_nums, count


def uniqueElements(records):
    """ Return the number of unique elements in a list.
    Inputs: list of phone numbers
    Output: number of unique telephone numbers
    """
    unique_nums = set()
    count = 0
    for record in records:
        for element in record:
            unique_nums, count = updateSet(unique_nums, count, element[0])
            unique_nums, count = updateSet(unique_nums, count, element[1])
    return count


def numOfUniqueTelephoneNums(records):
    """ Return the number of telephone numbers in a list of records (texts or calls).
    Inputs: List of set of records
    Output: number of unique telephone numbers
    """
    total_unique = uniqueElements(records)
    return total_unique


total_unique = numOfUniqueTelephoneNums([calls, texts])
print("There are {} different telephone numbers in the records.".format(total_unique))
