from itertools import product

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

    moves = [(-1,0),
            (1,0),
            (0,-1),
            (0,1)]
    
    #stores return values, used for checking if current coord is a perimter
    rsts = []

    #run recursively for each direction to move
    for move in moves:
        rsts.append(regionFind((coord[0]+move[0],coord[1]+move[1]),grid,metric,unvisited))

    #if coord + move returns 0, you're on a perimter cell
    for rst in rsts:
        if rst == 0:
            metric["perimeterCoords"].add(coord)

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
    metric = {"char":startingChar,"area":0,"perimeter":0,"perimeterCoords":set()}
    regionFind(start,grid,metric,unvisited)
    results.append({zone:metric})
    zone+=1

print(results)

day1 = 0
for item in results:
    for zone in item:
        day1+=item[zone]["area"]*item[zone]["perimeter"]

print(day1)



