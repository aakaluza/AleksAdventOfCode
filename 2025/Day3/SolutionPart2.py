########################################
#  Advent of Code 2025 Day 3
#  Solution for Part 2
#  Author: Alek Kaluza
########################################
from collections import defaultdict

def evaulateBank(bank: str) -> int:
    indexMap = defaultdict(list)

    for i in range(0, len(bank), 1):
        currNum = int(bank[i])
        indexMap[currNum].append(i)

    keys = sorted(indexMap.keys())
    

    return 0

def main():
    result = 0

    with open("/Users/alekkaluza/Projects/AleksAdventOfCode/2025/Day3/puzzleInput.txt", "r") as input:
        for line in input:
            result += evaulateBank(line.strip())
    
    with open("solutionPartTwo.txt", "w") as solution:
        solution.write(f'Alek\'s Solution: {result}\n')

main()