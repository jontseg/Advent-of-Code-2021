


import functools
from itertools import compress
# open text file input
with open('input.txt') as f:
    lines = f.readlines()
# create input array of numbers
    numlist = []
for num in lines:
    num = num.split()
    # print(num[0])
    if num[0].isdigit():
        numlist.append(int(num[0]))
# Create a list holding True and False values corresponding to indexes in original num list that satisfy constraint value at current
# is greater than value at previous index, place True at specified index. Place false at indexes that do not satisfy contraint.
# Compress list of True and False Values to only have True values, using the list of True/False values as selector
# return length of list of only True values remaining
# n = len(numlist)
# print(list(sum(numlist[i:i+3]) for i in range(n-3)))

print(len(list(compress([(int(sub1) < int(sub2)) for sub1, sub2 in zip(numlist, numlist[1:])], [(int(sub1) < int(sub2)) for sub1, sub2 in zip(numlist, numlist[1:])]))))

# res = list(compress([(int(sub1) < int(sub2)) for sub1, sub2 in zip(list(sum(numlist[i:i+3]) for i in range(len(numlist)-3)), list(sum(numlist[i:i+3]) for i in range(len(numlist)-3))[1:])], [(int(sub1) < int(sub2)) for sub1, sub2 in zip(list(sum(numlist[i:i+3]) for i in range(len(numlist)-2)), list(sum(numlist[i:i+3]) for i in range(len(numlist)-2))[1:])]))

# Part 2
print(len(list(compress([(int(sub1) < int(sub2)) for sub1, sub2 in zip(list(sum(numlist[i:i+3]) for i in range(len(numlist)-2)), list(sum(numlist[i:i+3]) for i in range(len(numlist)-3))[1:])], [(int(sub1) < int(sub2)) for sub1, sub2 in zip(list(sum(numlist[i:i+3]) for i in range(len(numlist)-2)), list(sum(numlist[i:i+3]) for i in range(len(numlist)-2))[1:])]))))