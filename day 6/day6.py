
cursorSyms = ["^",">","v","<"] #cursors in order of how the cursor moves
currentCursor = 0 #int of which curor symbol the cursor is set to
pos = (0,0) #position of cursor
motion = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)} #map of cursor index and unit motion
visited = set() #set of coordinates guard has been too


def checkMapEdge(map,pos,currentCursor):
    #check if on boundary and about to head off of boundary
    #return true if on map and can continue, return false if can't take another step
    r = len(map)
    c = len(map[0])
    
    if ((pos[0]==0 and currentCursor==0) or #top row going up 
        (pos[0]==r-1 and currentCursor==2) or #bottom row going down
        (pos[1]==0 and currentCursor==3) or #left col going left
        (pos[1]==c-1 and currentCursor==1) #right col going right
        ):
        return False
    else:
        return True
    
def incrementCursor(currentCursor):
    if currentCursor<3:
        return currentCursor + 1
    else:
        return 0

def determineOrientation(map,pos,currentCursor,motion):
    
    for test in range(3): #can only rotate 3 times, if a ublocked position isn't found by the 3rd rotation, return -1
        nextPos = getNextPos(pos,currentCursor,motion)

        #get next char
        nextChar = map[nextPos[0]][nextPos[1]]
        if nextChar == "#":
            currentCursor = incrementCursor(currentCursor)
            continue
        # if next spot isn't a #, return the current cursor
        return currentCursor
    
    return -1 # no valid orientation available

def getNextPos(pos,currentCursor,motion):
    #get cursor motion
    vert,lat = motion[currentCursor]
    return (pos[0]+vert,pos[1]+lat)

def printMap(map,pos,currentCursor):

    for i in range(len(map)):
        for j in range(len(map[0])):
            if (i,j)==pos:
                print(cursorSyms[currentCursor],end="")
            else:
                print(map[i][j],end="")
        print("\n")


#read in data
with open("input.txt","r") as file:
    map = []
    for i,line in enumerate(file):
        map.append([])
        for j,char in enumerate(line):
            if char == "\n":
                break
            if char in cursorSyms:
                pos = (i,j)
                currentCursor = cursorSyms.index(char)
                map[i].append(".")
                continue #don't append v character to map
            map[i].append(char)

pt1ans = 0
while True:
    #printMap(map,pos,currentCursor)
    onMap=True
    visited.add(pos)

    #check wheter you are about to go off map
    onMap = checkMapEdge(map,pos,currentCursor)

    #next move removes you from map 
    if onMap==False:
        break

    #determine next valid orientation, 
    currentCursor = determineOrientation(map,pos,currentCursor,motion)

    #update cursor pos
    pos = getNextPos(pos,currentCursor,motion)
    
pt1ans = len(visited)
print(f"pt1: {pt1ans}")


