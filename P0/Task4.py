"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

texts_sender = set()
texts_receiver = set()

for i in range(len(texts)):
    texts_sender.add(texts[i][0])
    texts_receiver.add(texts[i][1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

a_party = set()
b_party = set()

for i in range(len(calls)):
    a_party.add(calls[i][0])
    b_party.add(calls[i][1])

non_telemarketers = texts_sender | texts_receiver | b_party
telemarketers = set()

for i in a_party:
    if i not in non_telemarketers:
        telemarketers.add(i)
print("These numbers could be telemarketers: \n {}".format('\n'.join(sorted(telemarketers))))

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

