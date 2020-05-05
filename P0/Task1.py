"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import time
import csv

start = time.time()

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

all_numbers = a_party | b_party | texts_sender | texts_receiver
print(f"There are {len(all_numbers)} different telephone numbers in the records.")
end = time.time()
print(f"Execution time is {end - start:.4f} seconds")
"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
