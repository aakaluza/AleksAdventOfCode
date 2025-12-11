########################################
#  Advent of Code 2025 Day 2
#  Solutions for Parts 1 and 2
#  Author: Alek Kaluza
########################################

def evaluateRange(start: int, end: int) -> int:
    sum = 0

    for i in range(start, end + 1, 1):
        stringNumber = str(i)
        
        if len(stringNumber) % 2 == 1: continue
        
        halfPoint = len(stringNumber) // 2

        if (stringNumber[:halfPoint] == stringNumber[halfPoint:]): sum += i

    return sum

def main():
    with open("puzzleInput.txt", "r") as input:
        ranges = input.read().split(',')
        
        sum = 0

        for range in ranges:
            endPoints = range.split('-')
            startPoint = int(endPoints[0])
            endPoint = int(endPoints[1])
            sum += evaluateRange(startPoint, endPoint)

    with open("solution.txt", "w") as solution:
        solution.write(f'Alek\'s Solution: {sum}\n')

main()