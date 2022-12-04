import sys

sys.stdin = open('in.txt','r')
sys.stdout = open('out.txt','w')

fin = open('in.txt','r')

fdata = fin.read().split('\n')
print(fdata)
data = []
temp = []
for i in fdata:
    if i!='':
        temp.append(int(i))
    else:
        data.append(temp)
        temp = []

calories = []

for i in data:
    calories.append(sum(i))

t_calories = 0

# print(max(calories))
# t_calories += max(calories)
# calories.remove(max(calories))
# print(max(calories))
# t_calories += max(calories)
# calories.remove(max(calories))
# print(max(calories))
# t_calories += max(calories)
# calories.remove(max(calories))

# print(t_calories)