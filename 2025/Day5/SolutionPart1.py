########################################
#  Advent of Code 2025 Day 5
#  Solution for Part 1
#  Author: Alek Kaluza
########################################

def main():
    result = 0

    with open("puzzleInput.txt", "r") as input:
        ranges = []
        line = input.readline().strip()

        while line != "":
            range = line.split("-")
            ranges.append((int(range[0]), int(range[1])))
            line = input.readline().strip()
        
        line = input.readline().strip()
        while line != "":
            line = int(line)
            for r in ranges:
                if r[0] <= line <= r[1]:
                    result += 1
                    break
            line = input.readline().strip()
        
    with open("solutionPartOne.txt", "w") as solution:
        solution.write(f'Alek\'s Solution: {result}\n')

main()