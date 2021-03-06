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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电
请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

a= []

for call in calls:   #judge if it is ceded by 140
    validation = True
    if call[0][0] == '1'and call[0][1] == '4' and call[0][2] == '0':
        if call[0] not in a:
            a.append(call[0])
    else:
        if call[0] not in a:
            for text in texts:
                if call[0] != text[0] and call[0] != text[1]:  #never send or receive text
                    continue
                else:
                    validation = False
                    break
            if(validation):
                for call2 in calls:
                    valid = True
                    if call[0] != call2[1]: #never take a phone call
                        continue
                    else:
                        valid = False
                        break
                if(valid):
                    a.append(call[0])


a = sorted(a)

print("These numbers could be telemarketers: ")
for i in range(len(a)):
    print(a[i])