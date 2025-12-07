from itertools import product
from collections import defaultdict

def regionFind(coord:tuple,grid:list[list],metric:dict,unvisited:set[tuple]):

    #if the coord isn't the char of the region or you're outside the bounds of the grid, you've hit a permiter
    if (coord[0]<0 or
        coord[1]<0 or
        coord[0]>len(grid)-1 or
        coord[1]>len(grid[0])-1):
        metric["perimeter"]+=1
        return 0
    
    if grid[coord[0]][coord[1]] != metric["char"]:
        metric["perimeter"]+=1
        return 0
    
    #if you've been here before, don't add to the area and return
    if coord not in unvisited:
        return -1
    
    #else add to area, say, you've visited, and repeat function
    unvisited.remove(coord)
    metric["area"]+=1


    moves = [(-1,0,"u"),
            (1,0,"d"),
            (0,-1,"l"),
            (0,1,"r")]
    
    #stores return values, used for checking if current coord is a perimter
    rsts = []

    #run recursively for each direction to move
    for move in moves:
        result = regionFind((coord[0]+move[0],coord[1]+move[1]),grid,metric,unvisited)
        rsts.append((result,move[2]))

    #if coord + move returns 0, you're on a perimter cell
    for rst in rsts:
        direc = rst[1]
        if rst[0] == 0:
            #add to perimeters
            metric["perimeterCoords"].add(coord)
            #add to sides
            metric["sidesCoords"][direc].add(coord)


    # this location is an area coord
    return 1

#define grid
grid = []

#read in grid
with open("input.txt","r") as file:
    for line in file:
        grid.append(list(line.strip()))

#create set of unique positinos to visit
rows = range(len(grid))
cols = range(len(grid[0]))
unvisited = set(product(rows,cols))

#get arbitary starting coordinate
results = []
zone = 1
while len(unvisited)>0:
    start = unvisited.pop()
    #add back in... these get removed in the function
    unvisited.add(start)
    startingChar = grid[start[0]][start[1]]
    metric = {"char":startingChar,"area":0,"perimeter":0,"sides":0,"perimeterCoords":set(),"sidesCoords":defaultdict(set)}
    regionFind(start,grid,metric,unvisited)
    results.append({zone:metric})
    zone+=1




#pt2
for item in results:
    for zone in item:
        
        metric = item[zone]
        sideCoords = metric["sidesCoords"]
        checked = set()

        sideCount = 0
        #define side relationship
        sideRels = {"u":(0,1),
                    "d":(0,1),
                    "l":(1,0),
                    "r":(1,0),}
        
        for sideDir in sideCoords:
            if sideDir in {"u","d"}:
                sortedPerm = sorted(sideCoords[sideDir],key=lambda x: (x[0],x[1]))
            if sideDir in {"l","r"}:
                sortedPerm = sorted(sideCoords[sideDir],key=lambda x: (x[1],x[0]))



            for i in range(len(sortedPerm)):

                #first side
                if i==0:
                    sideCount+=1
                    continue


                coord = sortedPerm[i]
                prevCoord = sortedPerm[i-1]
                nextMove = sideRels[sideDir]



                #next coord isn't next to previous coord meaning new side
                if (prevCoord[0]+nextMove[0],prevCoord[1]+nextMove[1]) != coord:
                    sideCount+=1
        
        #add side count to metric
        metric["sides"] = sideCount


day1 = 0
day2 = 0
print(results)
for item in results:
    for zone in item:
        print(f"char:{item[zone]['char']},sides:{item[zone]['sides']}")
        day1+=item[zone]["area"]*item[zone]["perimeter"]
        day2+=item[zone]["area"]*item[zone]["sides"]

print(day1)
print(day2)
        