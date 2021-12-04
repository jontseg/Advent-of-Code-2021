# import functools
# from itertools import compress

# open text file input
with open('day2input.txt') as f:
    lines = f.readlines()
# create input array of numbers
    dirlist = []
for dir in lines:
    dir = dir.split('\n')
    dirlist.append((dir[0]))
dirlist
print([sum(list(int(dir.split()[1]) for dir in dirlist if dir.split()[0] == "forward")),sum((list(1 * int(dir.split()[1]) for dir in dirlist if dir.split()[0] == "down"))) + sum((list(-1 * int(dir.split()[1]) for dir in dirlist if dir.split()[0] == "up")))])
