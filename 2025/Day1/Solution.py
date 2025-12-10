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
        rotatedPointer = pointer + distance
        pointer = (rotatedPointer) % 100

        if part == 1 and pointer == 0: password += 1

        if part == 2 and (rotatedPointer < 0 or rotatedPointer > 99):
            # Issue here is negatives
            # Lets do some math man cmon
            password += abs(rotatedPointer // 100)
    
    return password

def main():
    distances = []
    with open("/Users/alekkaluza/Projects/AleksAdventOfCode/2025/Day1/puzzleInput.txt", "r") as input:
        for line in input:
            direction = -1 if line[0] == 'L' else 1
            distance = int(line[1:]) * direction
            distances.append(distance)
    
    with open("/Users/alekkaluza/Projects/AleksAdventOfCode/2025/Day1/solution.txt", "w") as solution:
        for i in range(1, 3, 1):
            solution.write(f'Alek\'s Part {i} Solution: {rotateLock(i, distances)}\n')

main()