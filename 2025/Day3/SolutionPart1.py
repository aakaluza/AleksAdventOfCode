########################################
#  Advent of Code 2025 Day 3
#  Solution for Part 1
#  Author: Alek Kaluza
########################################

def evaluateBank(bank: str) -> int:
    l = 0
    r = 1

    maxVoltage = 0

    while r < len(bank):
        currLeft = int(bank[l])
        currRight = int(bank[r])

        currVoltage = currLeft * 10 + currRight

        if currVoltage > maxVoltage:
            maxVoltage = currVoltage
        
        if currRight > currLeft:
            l = r
        
        r += 1
    
    return maxVoltage

def main():
    totalOutput = 0
    with open("puzzleInput.txt", "r") as input:
        for line in input:
            totalOutput += evaluateBank(line.strip())
    
    with open("solutionPartOne.txt", "w") as solution:
        solution.write(f'Alek\'s Solution: {totalOutput}\n')

main()