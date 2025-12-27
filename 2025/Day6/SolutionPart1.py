########################################
#  Advent of Code 2025 Day 6
#  Solution for Part 1
#  Author: Alek Kaluza
########################################

def main():
    result = 0
    with open("puzzleInput.txt", "r") as input:
        lines = input.readlines()
        ops = lines[len(lines) - 1].strip().split()
        results = [1 if op == '*' else 0 for op in ops] 

        for i in range(0, len(lines) - 1, 1):
            currLine = lines[i].strip().split()
            for j in range(0, len(currLine), 1):
                if ops[j] == '+':
                    results[j] += int(currLine[j])
                if ops[j] == '*':
                    results[j] *= int(currLine[j])
        
        result = sum(results)

    with open("solutionPartOne.txt", "w") as solution:
        solution.write(f'Alek\'s Solution: {result}')
    

main()