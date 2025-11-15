from collections import defaultdict
import itertools

def onBoard(coord:tuple,mapEdge:tuple) -> bool:
    onBoard = True
    if coord[0]<0 or coord[1]<0 or coord[0]>mapEdge[0] or coord[1]>mapEdge[1]:
        onBoard = False
    return onBoard

anntenas = defaultdict(list)
antiNode = set() #unique csys of antinodes
with open("input.txt","r") as file:
    map = []
    for r,line in enumerate(file.readlines()):
        line = line.strip()
        map.append([])
        for c,char in enumerate(line):
            map[-1].append(char)
            if char != ".":
                anntenas[char].append((r,c))

#edge of map
mapEdge = (len(map)-1,len(map[0])-1)

# use itertools to create permutations of pairs based on how many anntennas there are. 
# the idea is for each pair of antennas find the r and c diff between them, you should then be able to add/subtract that diff from from each anntena to find an antinode
# there will be a check to make sure that the coordinates are actually on the board. 
# need a convention so we don't have to check the two nodes that will get generated that are between the antenna

for anntena in anntenas:

    #get combo of anntennas where you need to find antinodes
    combos = list(itertools.combinations(range(len(anntenas[anntena])),2))
    
    #get r,c for the two anntennas
    for combo in combos:
        anntena1 = anntenas[anntena][combo[0]]
        anntena2 = anntenas[anntena][combo[1]]
    
        #find difference between anntena1 and anntena2
        rDiff = anntena2[0] - anntena1[0]
        cDiff = anntena2[1] - anntena1[1]

        #create antinodes
        a1 = (anntena1[0]-rDiff,anntena1[1]-cDiff)
        a2 = (anntena2[0]+rDiff,anntena2[1]+cDiff)

        if onBoard(a1,mapEdge):
            antiNode.add(a1)
        if onBoard(a2,mapEdge):
            antiNode.add(a2)

print(len(antiNode))