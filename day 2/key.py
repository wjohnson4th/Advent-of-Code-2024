with open("input.txt") as file:
    lines = file.readlines()

def IsOkay(x):
    increasing = True if int(x[1]) > int(x[0]) else False
    diffAllowed = [1, 2, 3] if increasing else [-1, -2, -3]
    
    for i in range(1, len(x)):
        if int(x[i]) - int(x[i - 1]) not in diffAllowed:
            return 0
    return 1

partOne = 0
partTwo = 0

for line in lines:
    line = line.strip().split()
    if IsOkay(line):
        partOne += 1
    else:
        for i in range(len(line)):
            newline = line.copy()
            del newline[i]
            if IsOkay(newline):
                partTwo += 1
                break

print("PART 1 SOLUTION - " + str(partOne))
print("PART 2 SOLUTION - " + str(partOne + partTwo))
