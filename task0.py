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
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

""" 第一句： 输出短信记录的第一条 output the first record of texts"""
print("First record of texts, " + texts[0][0] + " texts " + texts[0][1] + " at time " + texts[0][2])

""" 第二句： 输出通话记录的最后一条  output the last record of calls"""
i= 0
for call in calls:
    if(i == (len(calls) - 1)):
        print("Last record of calls, " + call[0] + " calls " + call[1] + " at time " + call[2] + ", lasting " + call[3] + " seconds")
    i+=1