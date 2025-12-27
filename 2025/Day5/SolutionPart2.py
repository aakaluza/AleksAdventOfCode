########################################
#  Advent of Code 2025 Day 5
#  Solution for Part 2
#  Author: Alek Kaluza
########################################
class Range:
    def __init__(self, start: int, end: int):
        self.startPoint = start
        self.endPoint = end
    
    def __sizeof__(self) -> int:
        return self.endPoint - self.startPoint + 1

def insertRange(ranges: list[Range], newRange: Range):
    i = 0
    while i < len(ranges) and newRange.startPoint > ranges[i].startPoint:
        i += 1

    ranges.insert(i, newRange)

def mergeRanges(ranges: list[Range]):
    l = 0
    r = 1

    while r < len(ranges):
        lastMerged = ranges[l]
        current = ranges[r]
        if current.startPoint <= lastMerged.endPoint:
            lastMerged.endPoint = max(current.endPoint, lastMerged.endPoint)
            ranges.pop(r)
        else:
            l = r
            r += 1

def main():
    numFreshIngredients = 0
    ranges = []

    with open("puzzleInput.txt", "r") as input:
        line = input.readline().strip()
        while line != "":
            endPoints = line.split("-")
            newRange = Range(int(endPoints[0]), int(endPoints[1]))
            insertRange(ranges, newRange)
            line = input.readline().strip()     
    
        mergeRanges(ranges)

        for range in ranges:
            numFreshIngredients += range.__sizeof__()
    
    with open("solutionPartTwo.txt", "w") as solution:
        solution.write(f'Alek\'s Solution: {numFreshIngredients}\n')

main()