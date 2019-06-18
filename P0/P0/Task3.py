import re

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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def findOutgoingCallsFromBangalore(calls):
    bangalore_calls = []
    for call in calls:
        if '(080)' in call[0]:
            bangalore_calls.append(call)
    return bangalore_calls


def getAreaCode(num):
    if ' ' in num:
        return num[:4]
    if '(' in num:
        return re.search('\([0-9]+\)', num).group(0)
    if '140' in num[:3]:
        return num[:3]
    return ''


def receivingNumsSortedPrefixes(calls):
    area_codes_set = set()
    for call in calls:
        receiving_num = call[1]
        area_code = getAreaCode(receiving_num)
        if area_code not in area_codes_set:
            area_codes_set.add(area_code)
    return sorted(area_codes_set)

def percentageCallsToBangalore(calls):
    count = 0;
    for call in calls:
        if '(080)' in call[1]:
            count += 1
    return (count / len(calls)) * 100


bangalore_calls = findOutgoingCallsFromBangalore(calls)
codes = receivingNumsSortedPrefixes(bangalore_calls)
print("The numbers called by people in Bangalore have codes:")
for code in codes:
    print(code)

print("{:0.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentageCallsToBangalore(calls)))
