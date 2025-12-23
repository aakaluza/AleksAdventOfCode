########################################
#  Advent of Code 2025 Day 4
#  Solution for Part 2
#  Author: Alek Kaluza
########################################

def calculateAdjacencies(warehouse: list[list[int]]) -> int:
    result = 0
    updatedResult = 0

    while(True):
        removedIndices = []

        for i in range(1, len(warehouse) - 1, 1):
            for j in range(1, len(warehouse[i]) - 1, 1):
                if warehouse[i][j] == 1:
                    sum = warehouse[i-1][j-1] + warehouse[i-1][j] + warehouse[i-1][j+1] + warehouse[i][j-1] + warehouse[i][j+1] + warehouse[i+1][j-1] + warehouse[i+1][j] + warehouse[i+1][j+1]
                    if (sum < 4):
                        updatedResult += 1
                        removedIndices.append((i, j))

        if updatedResult == 0 or len(removedIndices) == 0:
            return result
        else:
            result += updatedResult
            updatedResult = 0

            for pair in removedIndices:
                warehouse[pair[0]][pair[1]] = 0

def main():
    warehouse = []
    copy = []

    with open("puzzleInput.txt", "r") as input:
        rowLength = 0
        for line in input:
            row = [0]
            for c in line.strip():
                row.append(1 if c == '@' else 0)
            row.append(0)
            warehouse.append(row)

            rowLength = len(row)
        
        warehouse.insert(0, [0] * rowLength)
        warehouse.append([0] * rowLength)
        

    with open("solutionPartTwo.txt", "w") as solution:
        result = calculateAdjacencies(warehouse)
        solution.write(f'Alek\'s Solution: {result}\n') 

main()