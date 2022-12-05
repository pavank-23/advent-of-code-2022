import sys

sys.stdout = open('out.txt','w')

fin = open('in.txt','r')

fdata = fin.read().split('\n')
# print(fdata)

data = []

for i in fdata:
    pairs = i.split(',')
    # print(pairs)``
    x = set([j for j in range(int(pairs[0].split('-')[0]),int(pairs[0].split('-')[1])+1)])
    y = set([j for j in range(int(pairs[1].split('-')[0]),int(pairs[1].split('-')[1])+1)])
    data.append([x,y])

count = 0

for i in data:
    if i[0].intersection(i[1]) == i[0] or i[0].intersection(i[1]) == i[1]:
        count += 1

print(count)