"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

def updateDurationRegistry(d, num, duration):
    if num in d:
        d[num] += duration
    else:
        d[num] = duration
    return d

def longestTimeOnPhone(calls):
    duration_dict = {}
    for call in calls:
        duration_dict = updateDurationRegistry(duration_dict, call[0], int(call[3]))
        duration_dict = updateDurationRegistry(duration_dict, call[1], int(call[3]))
    num_with_longest_call = max(duration_dict, key=duration_dict.get)
    longest_call_duration = duration_dict[num_with_longest_call]
    return num_with_longest_call, longest_call_duration


print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*longestTimeOnPhone(calls)))
