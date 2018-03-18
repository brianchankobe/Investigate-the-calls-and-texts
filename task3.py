"""
Intro to Python Lab 1, Task 3
Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo.
Full submission instructions are available on the Lab Preparation page.
"""

"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
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

"""

phlist = {}



j = 1
for call in calls:
    if(call[0][0] == '(' and call[0][1] == '0' and call[0][2] == '8' and call[0][3] == '0'): #confirm whether it is called by bangalore(080)
        if call[1][0] == '(':  #is it fixed number
            i = 1
            phlist[str(j)] = call[1][i]
            i+=1
            while call[1][i] != ')':   #output the area code
                phlist[str(j)] += call[1][i]
                i+=1
            j += 1
        elif call[1][0] == '1'and call[1][1] == '4' and call[1][2] == '0': #it is telemarketers' number
            phlist[str(j)] = '140'
            j += 1
        else: #it is mobile phone number
            phlist[str(j)] = call[1][0]
            for element in range(3):
                phlist[str(j)] += call[1][element+1]
            j += 1

codeAll = []  #all the area number

for ph in phlist:
    if phlist[ph] not in codeAll:
        codeAll.append(phlist[ph])


codeCompare = sorted(codeAll)

print("The numbers called by people in Bangalore have codes: ")
for i in range(len(codeCompare)):
    print(codeCompare[i])

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?
Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

count = 0 #calculate times from 080 to 080
for ph in phlist:
    if phlist[ph] == '080':
        count += 1

callPerc = (count / len(phlist))*100
print("\n{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(callPerc, 2)))