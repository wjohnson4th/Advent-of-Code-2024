hits = []

def checkDiag(map,i,j,r,c,word:str):

    #assumes ij position in matrix is centered at middle of word

    flag = 1

    #grab center letter
    idx = int((len(word))/2)
    centerLetter = word[idx]

    #if ij position isn't centerletter, isn't a crossing
    if map[i][j]!=centerLetter:
        return 0

    #if i or j are out of bounds, return 0
    iS = [i,i+1,i-1]
    jS = [j,j+1,j-1]

    for ii in iS:
        if ii not in range(r):
            return 0 
    for jj in jS:
        if jj not in range(c):
            return 0

    #check if TL -> BR diag is met
    result = map[i-1][j-1] + map[i][j] +map[i+1][j+1]
    if result != word and result != word[::-1]:
        return 0
    #check if BL -> TR diag is met
    result = map[i-1][j+1] + map[i][j] +map[i+1][j-1]
    if result != word and result != word[::-1]:
        return 0
    
    #all checks passed return 1
    return flag



word = "MAS"

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

count = 0
wordLen = len(word)
for i in range(r):
    for j in range(c):
        if i==1 and j==2:
            pass
        count += checkDiag(map,i,j,r,c,word)



print(count)




"""
for hit in hits:
    print(hit)

for row in testMap:
    for letter in row:
        print(letter,end="")
    print("\n")
"""