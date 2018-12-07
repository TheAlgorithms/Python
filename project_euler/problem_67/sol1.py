import os
import sys
path = os.path.join(sys.path[0], 'p067_triangle.txt')
with open(path) as f:
    lines = f.readlines()
current_best_path = [0]
for line in lines:
    line = [int(i) for i in line.strip().split(' ')]
    new_best_path = [] #list representing the best path ending in each location in the next line
    for index,element in enumerate(line):
        if index == 0:
            new_best_path.append(current_best_path[0]+line[0])
        elif index == len(line)-1:
            new_best_path.append((current_best_path[-1] + line[index]))
        else:
            new_best_path.append(max(current_best_path[index-1],current_best_path[index])+line[index])
    current_best_path = new_best_path[:]

assert max(current_best_path) == 7273
