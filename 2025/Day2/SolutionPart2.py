########################################
#  Advent of Code 2025 Day 2
#  Solution for Part 2
#  Author: Alek Kaluza
########################################

def evaluateNumber(number: int) -> int:
    numAsString = str(number)
    numLength = len(numAsString)

    for i in range(1, numLength // 2 + 1):
        if numLength % i == 0:
            substring = numAsString[0:i]
            if numAsString == substring * (numLength // i):
                return number
    
    return 0

def evaluateRange(start: int, end: int) -> int:
    sum = 0

    for num in range(start, end + 1, 1):
        sum += evaluateNumber(num)

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

    with open("solutionPartTwo.txt", "w") as solution:
        solution.write(f'Alek\'s Solution: {sum}\n')

main()