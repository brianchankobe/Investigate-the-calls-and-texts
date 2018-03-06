"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records.
"""

a = []
""" calculate the amount of different phone numbers in texts (repeated numbers just output once)"""
for text in texts:
    if text[0] not in a:
        a.append(text[0])
    if text[1] not in a:
        a.append(text[1])

""" calculate the amount of different phone numbers in calls (repeated numbers just output once)"""
for call in calls:
    if call[0] not in a:
        a.append(call[0])
    if call[1] not in a:
        a.append(call[1])

print("There are " + str(len(a)) + " different telephone numbers in the records")
