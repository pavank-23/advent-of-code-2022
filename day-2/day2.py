import sys

# sys.stdin = open('in.txt','r')
sys.stdout = open('out.txt','w')

# A - Y, B - Z, C - X
fin = open('in.txt','r')

fdata = fin.read().split('\n')

score = 0

for i in fdata:
    # if i[2] == 'X': score += 1
    # if i[2] == 'Y': score += 2
    # if i[2] == 'Z': score += 3

    # if i[2] == 'X' and i[0] == 'C': score += 6
    # if i[2] == 'X' and i[0] == 'A': score += 3
    # if i[2] == 'Y' and i[0] == 'A': score += 6
    # if i[2] == 'Y' and i[0] == 'B': score += 3
    # if i[2] == 'Z' and i[0] == 'B': score += 6
    # if i[2] == 'Z' and i[0] == 'C': score += 3


    if i[2] == 'Y':
        if i[0] == 'A' : score += 4
        if i[0] == 'B' : score += 5
        if i[0] == 'C' : score += 6

    elif i[2] == 'Z':
        if i[0] == 'A' : score += 8
        if i[0] == 'B' : score += 9
        if i[0] == 'C' : score += 7

    else:
        if i[0] == 'A' : score += 3
        if i[0] == 'B' : score += 1
        if i[0] == 'C' : score += 2

print(score)