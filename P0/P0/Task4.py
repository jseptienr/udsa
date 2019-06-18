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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def getIncomingOutgoingSets(records):
    outgoing = set()
    incoming = set()
    for record in records:
        if record[0] not in outgoing:
            if '140' not in record[0][:3]:
                outgoing.add(record[0])
        if record[1] not in incoming:
            incoming.add(record[1])
    return outgoing, incoming


def findTelemarketingNumbers(calls, texts):
    out_calls, in_calls = getIncomingOutgoingSets(calls)
    out_texts, in_texts = getIncomingOutgoingSets(texts)
    diff = out_calls - in_calls - out_texts - in_texts
    return sorted(diff)

telemarketers = findTelemarketingNumbers(calls, texts)
print("These numbers could be telemarketers: ")
for num in telemarketers:
    print(num)
