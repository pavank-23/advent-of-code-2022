import sys

sys.stdout = open('out.txt','w')

fin = open('in.txt','r')

fdata = fin.read().split('\n')
# print(fdata)

# sum = 0

# for i in fdata:
#     common = (set(i[:len(i)//2]).intersection(set(i[len(i)//2:]))).pop()
#     if ord(common)>=97:
#         sum += ord(common)-96
#     else:
#         sum += ord(common)-38
    
# print(sum)

groups = []
badge_sum = 0

for i in range(0,len(fdata)-2,3):
    groups.append([fdata[i],fdata[i+1],fdata[i+2]])

# print(groups)

for group in groups:
    common =(set(group[0]).intersection(set(group[1])).intersection(set(group[2]))).pop()
    if ord(common)>=97:
        badge_sum += ord(common) - 96
    else:
        badge_sum += ord(common) - 38

print(badge_sum)