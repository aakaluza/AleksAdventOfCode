########################################
#  Advent of Code 2025 Day 4
#  Solution for Part 1
#  Author: Alek Kaluza
########################################

def calculateAdjacencies(warehouse: list[list[int]]) -> int:
    result = 0


    for i in range(1, len(warehouse) - 1, 1):
        for j in range(1, len(warehouse[i]) - 1, 1):
            if warehouse[i][j] == 1:
                sum = warehouse[i-1][j-1] + warehouse[i-1][j] + warehouse[i-1][j+1] + warehouse[i][j-1] + warehouse[i][j+1] + warehouse[i+1][j-1] + warehouse[i+1][j] + warehouse[i+1][j+1]
                if (sum < 4):
                    result += 1
    
    return result


def main():
    matrix = []

    with open("puzzleInput.txt", "r") as input:
        rowLength = 0
        for line in input:
            row = [0]
            for c in line.strip():
                row.append(1 if c == '@' else 0)
            row.append(0)
            matrix.append(row)

            rowLength = len(row)
        
        matrix.insert(0, [0] * rowLength)
        matrix.append([0] * rowLength)
        

    with open("solutionPartOne.txt", "w") as solution:
        result = calculateAdjacencies(matrix)
        solution.write(f'Alek\'s Solution: {result}\n') 

main()