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

number_dict = dict()
for i in range(len(calls)):
    if calls[i][0] not in number_dict:
        number_dict[calls[i][0]] = int(calls[i][-1])
    else:
         number_dict[calls[i][0]] += int(calls[i][-1])

    if calls[i][1] not in number_dict:
        number_dict[calls[i][1]] = int(calls[i][-1])
    else:
         number_dict[calls[i][1]] += int(calls[i][-1])


max_duration = 0
for number, duration in number_dict.items():
    if duration > max_duration:
        max_duration = duration
        answer = number

print(f"{answer} spent the longest time, {max_duration} seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

