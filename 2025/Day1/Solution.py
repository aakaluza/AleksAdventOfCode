password = 0
pointer = 50

def rotateLock(distance: int):
    global password
    global pointer

    pointer = ((pointer + distance) + 100) % 100
    if pointer == 0: password += 1

def main():
    global password

    with open("puzzleInput.txt", "r") as input:
        for line in input:
            direction = -1 if line[0] == 'L' else 1
            distance = int(line[1:]) * direction

            rotateLock(distance)
    
    with open("solution.txt", "w") as solution:
        solution.write(f'Alek\'s Solution: {password}')

main()