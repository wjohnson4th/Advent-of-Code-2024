import time

rstCache = {}

def increment(value:int) -> list[int]:
    #take in an int an return a list of results

    #if it's an even number then split them up into two different ints
    valuestr = str(value)
    n = len(valuestr)

    #if value = 0 increment by 1
    if value==0:
        ans = [1]
    
    elif n%2==0:
        ans = [int(valuestr[0:n//2]),int(valuestr[n//2:])]
    
    # else return the number multiplied by 2024
    else:
        ans = [value*2024]

    return ans
    
def incrementV2(value:int,n:int) -> int:
    #returns the number of unique ints for a given value that needs to be iterated n times
    #value = int to go through increment algorithm
    #n = number of times needing to be iterated on

    #if value in cache, return number of stones
    if (value,n) in rstCache:
        return rstCache[(value,n)]

    if n == 1:
        rst = increment(value)
        ans = len(rst)
        rstCache[(value,1)] = ans
        return ans
    
    else:
        #initialize value in cache
        rstCache[(value,n)] = 0
        #get results of query
        rsts = increment(value)
        for rst in rsts:
            #initialize value in cache
            rstCache[(value,n)] += incrementV2(rst,n-1)

        return rstCache[(value,n)]


    



start = time.perf_counter()

with open("input.txt","r") as file:
    initial = list(map(int,file.readline().split(" ")))

#maybe try and optimize for 0? 
#if you see a zero, you can quickly determine how many rocks that will turn into
#once you hit a zero
#ok even just starting with a zero suffers the same challenges as you try and get out to 70
#is there a way we can analyze the rules to make out a pattern that's more determistic?



cycles = 75
arr = initial
count = 0

for item in arr:
    count += incrementV2(item,cycles)

end = time.perf_counter()
elapsed = end-start

print(count)
print(elapsed)