"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

all_numbers = set()

for i in range(len(texts)):
    all_numbers.add(texts[i][0])
    all_numbers.add(texts[i][1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

for i in range(len(calls)):
    all_numbers.add(calls[i][0])
    all_numbers.add(calls[i][1])

#all_numbers = a_party | b_party | texts_sender | texts_receiver
print(f"There are {len(all_numbers)} different telephone numbers in the records.")
"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
