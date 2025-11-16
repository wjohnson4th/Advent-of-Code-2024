
#define initial variables
grid = []
trailHeads = [] #list of coodinates of unique trailheads
peaks = set() #list of coordinates of unique peaks as a set for ease of checking


def trailSearch(coord:tuple,grid:list[list],uniquePeaks:set[tuple],trailRating:list):
    #this function takes a coordinate and returns the next valid coordinates along the trail
    #if there are no valid coordiates the function returns False
    #if there next coodinate is a 9 returns True
    

    #get current value
    r,c  = coord
    value = grid[r][c]

    #if value is equal to peak, this is a unique peak
    #add to uniquePeaks and return
    #if you got to a peak, this inidicates this is a unique trail increment trailRating
    if value == 9:
        uniquePeaks.add((r,c))
        trailRating[0]+=1
        return

    #next value is +1 the current value
    nextValue = value + 1

    #check the four adjacent directions
    
    #check top
    if r != 0 and grid[r-1][c]==nextValue:
        trailSearch((r-1,c),grid,uniquePeaks,trailRating)
    #check bottom
    if r != len(grid)-1 and grid[r+1][c]==nextValue:
        trailSearch((r+1,c),grid,uniquePeaks,trailRating)
    #check left
    if c != 0 and grid[r][c-1]==nextValue:
        trailSearch((r,c-1),grid,uniquePeaks,trailRating)
    #check right
    if c != len(grid[0])-1 and grid[r][c+1]==nextValue:
        trailSearch((r,c+1),grid,uniquePeaks,trailRating)

    #if you get to this point in the code that means there are not valid paths forward
    #return out of the function
    return
    





#read in data
with open("input.txt","r") as file:
    for r,line in enumerate(file):
        myInput = line.strip().split()
        row = list(map(int,*myInput))
        
        #get locations of trailheads
        for c,item in enumerate(row):
            if item == 0:
                trailHeads.append((r,c))

        #append row to grid
        grid.append(row)


#loop through trailheads

runSumPt1 = 0
runSumPt2 = 0

for trailHead in trailHeads:
    uniquePeaks = set() #keep track of unique peaks visited per trailhead
    trailRating = [0]
    r,c = trailHead
    trailSearch((r,c),grid,uniquePeaks,trailRating)
    runSumPt1 += len(uniquePeaks)
    runSumPt2 += trailRating[0]

print(runSumPt1)
print(runSumPt2)