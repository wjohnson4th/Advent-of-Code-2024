import time


def increment(value:int) -> list[int]:
    #take in an int an return a list of results
    
    #if value = 0 increment by 1
    if value==0:
        return [1]
    
    #if it's an even number then split them up into two different ints
    valuestr = str(value)
    n = len(valuestr)
    if n%2==0:
        return [int(valuestr[0:n//2]),int(valuestr[n//2:])]
    
    # else return the number multiplied by 2024
    return [value*2024]
    


start = time.perf_counter()

with open("input.txt","r") as file:
    initial = list(map(int,file.readline().split(" ")))


cycles = 25
arr = initial
for _ in range(cycles):
    newArr = []
    for item in arr:
        values = increment(item)
        for value in values:
            newArr.append(value)
    arr = newArr

end = time.perf_counter()

elapsed = end-start

print(len(arr))
print(elapsed)