from collections import defaultdict
import copy


#pseudo code
#start with postion and orientation
#determine next location where you would be required to stop
#do this by looking in the heading of the position, you will either find an obstacle or a map edge
#once you have found the next position, set that as the position
#add visited locations to visited set by creating a loop of values based on starting position and final position
#check whether you are on an edge
#if you are on an edge return off map
#get count of keys in visited set

class Guard:
    def __init__(self) -> None:
        self.motion = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)} #map of cursor index and unit motion
        self.cursorSyms = ["^",">","v","<"] #cursors in order of how the cursor moves

        self.positions = [] #recods in sequence all locations where cursor stopped for each new position
        self.visited = set()  #set of coordinates guard has been too
        self.obsR2C = defaultdict(lambda:set()) #Y location of obstalces in terms of X
        self.obsC2R = defaultdict(lambda:set()) #X location of obstacles in terms of Y
        self.atEdge = False # bool at edge
        self.inLoop = False # flag for if you have been in exact postion/orientation prior

        self.map:list[list] = [] #list or rows containing column data

    def setPos(self,pos:tuple,currentCursor)->None:
        posData = {
            "pos":pos,
            "currentCursor":currentCursor
        }
        self.positions.append(posData)

    def getPos(self,idx:int = -1) -> dict:
        #defaults to getting the last position unless specified
        return self.positions[idx]

    def returnAtEdge(self) -> bool:
        return self.atEdge
    
    def returnInLoop(self) -> bool:
        return self.inLoop

    def getNextCursor(self):
        pos = self.getPos()
        currentCursor = pos["currentCursor"]
        if currentCursor == len(self.cursorSyms)-1: #check whether you are at the last cursor
            return 0
        else:
            return currentCursor + 1
        
    def setNextPos(self) -> dict:
        #returns (r,c) of next position. will also set atEdge bool
        pos = self.positions[-1]["pos"]
        currentCursor = self.positions[-1]["currentCursor"]

        r = pos[0]
        c = pos[1]

        if currentCursor == 0: #moving up 
            try:
               r = max(x for x in self.obsC2R[c] if x<pos[0]) + 1
            except ValueError:
                self.atEdge = True
                r = 0

        if currentCursor == 2: #moving down 
            try:
               r = min(x for x in self.obsC2R[c] if x>pos[0]) - 1
            except ValueError:
                self.atEdge = True
                r = len(self.map)-1

        if currentCursor == 1: #moving right 
            try:
               c = min(x for x in self.obsR2C[r] if x>pos[1]) - 1
            except ValueError:
                self.atEdge = True
                c = len(self.map[0])-1

        if currentCursor == 3: #moving left 
            try:
               c = max(x for x in self.obsR2C[r] if x<pos[1]) + 1
            except ValueError:
                self.atEdge = True
                c = 0

        #increment cursor
        nextCursor =  self.getNextCursor()

        #set new position
        self.setPos((r,c),nextCursor)

        for position in self.positions[:-1]: #get all previous positions 
            if self.getPos() == position:
                self.inLoop=True

        #update the add visited
        self.addVisited()

        return self.getPos()

    def addVisited(self):
        curPos = self.getPos() #recently moved to position
        lastPos = self.getPos(-2) #get second to last position
        currentCursor = lastPos["currentCursor"] #get current sym which will be used for directions
        motionRow, motionColumn = self.motion[currentCursor]

        tempLoc = lastPos["pos"]
        while True:
            self.visited.add(tempLoc) #add location to visited
            if tempLoc == curPos["pos"]:
                break
            tempLoc = (tempLoc[0] + motionRow, tempLoc[1] + motionColumn)
            
    def printVisMap(self):
        position = self.getPos()
        pos = position["pos"]
        currentCursor = position["currentCursor"]
        for r,row in enumerate(self.map):
            for c,char in enumerate(row):
                if (r,c) == pos:
                    print(self.cursorSyms[currentCursor],end="")
                else:
                    print(char,end="")
            print("")#new line

        print("")#new line

    def addObs(self,r,c,char="#"):
        self.obsR2C[r].add(c)
        self.obsC2R[c].add(r)
        try:
            self.map[r][c] = char
        except:
            pass


myGuardPt1 = Guard()

#read in data
with open("input.txt","r") as file:
    for r,line in enumerate(file):
        myGuardPt1.map.append([])
        for c,char in enumerate(line):
            if char == "\n":
                break
            if char in myGuardPt1.cursorSyms:
                currentCursor=myGuardPt1.cursorSyms.index(char)
                myGuardPt1.setPos((r,c),currentCursor)
                myGuardPt1.map[r].append(".")
                continue #don't append v character to map
            if char == "#":
                myGuardPt1.addObs(r,c)
            myGuardPt1.map[r].append(char)

#copy of class object from start of each iteration. 
myGuardInitial = copy.deepcopy(myGuardPt1)

pt2AddedObstacles = set()
while True:

    #print vis map for trouble shooting
    #myGuardPt1.printVisMap()

    #get next position
    myGuardPt1.setNextPos()

    #iterate on each intermediate position between last start and 
    #current new location
    #grab current and second to last position
    curPos = myGuardPt1.getPos() #recently moved to position
    lastPos = myGuardPt1.getPos(-2) #get second to last position
    currentCursor = lastPos["currentCursor"] #get current sym which will be used for directions
    motionRow, motionColumn = myGuardPt1.motion[currentCursor]
    tempLoc = lastPos["pos"]
    while True:
        if tempLoc == curPos["pos"]:
            break
        tempLoc = (tempLoc[0] + motionRow, tempLoc[1] + motionColumn)
    
        #guard pt2
        myGuardPt2 = copy.deepcopy(myGuardInitial)

        #create obstacle at temp location
        myGuardPt2.addObs(tempLoc[0],tempLoc[1],char="O")

        while True:
            #myGuardPt2.printVisMap()
            myGuardPt2.setNextPos()

            if myGuardPt2.returnInLoop():
                pt2AddedObstacles.add((tempLoc[0],tempLoc[1]))
                #print(len(pt2AddedObstacles))
                #myGuardPt2.printVisMap()
                break
            if myGuardPt2.returnAtEdge():
                break

    #check if at edge or in loop to break out of loop
    if myGuardPt1.returnInLoop():
        break
    if myGuardPt1.returnAtEdge():
        break


print(f"pt1: {len(myGuardPt1.visited)}")
print(f"pt2: {len(pt2AddedObstacles)}")


