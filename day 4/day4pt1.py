import itertools

hits = []

def findWord(map,i,j,r,c,word,rowinc,colinc,testMap)->int:
    try:
        flag = 1
        for z,letter in enumerate(word):
            if map[i+z*rowinc][j+z*colinc]!=letter:
                return 0
            if i+z*rowinc<0 or i+z*rowinc>r:
                return 0
            if j+z*colinc<0 or j+z*colinc>c:
                return 0

        if flag == 1:
            hits.append((i,j,rowinc,colinc))

            for z,letter in enumerate(word):
                testMap[i+z*rowinc][j+z*colinc]=letter

        return flag
    except:
        return 0

word = "XMAS"

with open("input.txt","r") as file:
    map = file.readlines()
    map = [item.strip() for item in map]

#get rows and cols
r = len(map)
c = len(map[0])

testMap = []

for i in range(r):
    testMap.append([])
    for j in range(c):
        testMap[i].append(".")

#print(testMap)

count = 0
wordLen = len(word)
dirs = list(itertools.product([0,-1,1],repeat = 2))
dirs.remove((0,0))
for i in range(r):
    for j in range(c):
        for dir in dirs:
            count += findWord(map,i,j,r,c,word,dir[0],dir[1],testMap)



print(count)




"""
for hit in hits:
    print(hit)

for row in testMap:
    for letter in row:
        print(letter,end="")
    print("\n")
"""