########################################
#  Advent of Code 2025 Day 1
#  Solution for Both Parts
#  Author: Alek Kaluza
########################################
from typing import List

def rotateLock(part: int, distances: List[int]):
    password = 0
    pointer = 50

    for distance in distances:
        if part == 2:
            if distance > 0: password += (pointer + distance) // 100
            else: password += ((pointer * -1) % 100 + abs(distance)) // 100
        
        pointer = (pointer + distance) % 100

        if part == 1 and pointer == 0: password += 1
    
    return password

def main():
    distances = []
    with open("puzzleInput.txt", "r") as input:
        for line in input:
            direction = -1 if line[0] == 'L' else 1
            distance = int(line[1:]) * direction
            distances.append(distance)
    
    with open("solution.txt", "w") as solution:
        for i in range(1, 3, 1):
            solution.write(f'Alek\'s Part {i} Solution: {rotateLock(i, distances)}\n')

main()