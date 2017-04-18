'''n=raw_input('enter the number of record to fetch');
f=open('russia.txt','r');

column = []
arr1=[]
for line in f:
    column = line.split("|")
    column.append()
print column[2];'''
'''for data in column:
    print data[2];

print (arr1.sort())'''
'''file = open("russia.txt")

column = []  
arr=[]
arr1=[]
for line in file:
    column = line.split("|")
    arr.append(int(column[3]))
    #arr.append(column[3].sort());
print arr;


    sorted_data=sorted(f.readlines(),
                    key=lambda item: int(item.rsplit("|",1)[-2].strip()))
print (sorted_data)
with open("russia.txt", "r") as f:
    sorted_data = sorted(f.readlines(), key=lambda item: int(item.strip().split("|")[-1]))
    sort = ["|".join(line.strip().split("|")) for line in sorted_data]
    print(sorted)'''


import csv
import operator

c=0;
sample = open("india.txt")
csv1 = csv.reader(sample, delimiter='|')
sort = sorted(csv1, key=operator.itemgetter(3))
for eachline in sort:
    print eachline
    c=c+1;
    if c==10:
        break;


print "=========================================="

c=0;
sample = open("india.txt")
csv1 = csv.reader(sample, delimiter='|')
sort = sorted(csv1, key=operator.itemgetter(4))
for eachline in sort:
    print eachline
    c=c+1;
    if c==10:
        break;


sample.close();