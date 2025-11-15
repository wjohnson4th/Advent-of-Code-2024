
import itertools
import copy
from collections import defaultdict

def checkRstPt1(rst:int,digits:list,permutation) -> bool:
    #operations = ["+","*"]
    
    check = digits[0]

    for i in range(len(digits))[1:]:

        if permutation[i-1] == 0:
            check = digits[i] + check
        else:
            check = digits[i] * check


    return check == rst

def checkRstPt2(rst:int,digits:list,permutation) -> bool:
    #operations = ["+","*","||"]

    check = digits[0]

    for i in range(len(digits))[1:]:

        if permutation[i-1] == 0:
            check = digits[i] + check
        elif permutation[i-1] == 1:
            check = digits[i] * check
        else:
            check = int(str(check)+str(digits[i]))


    return check == rst

def checkRstOrderConsistant(rst:int,digits:list,permutation) -> bool:
    #operations = ["+","*"]
    check = 0

    #do multiplication first
    #get indexes where perumtation is multiplication
    multIndex = [i for i,x in enumerate(permutation) if x==1]
    #within multIndex group adjacent ints
    additionGroups:list[list] = []
    for i in range(len(digits)):
        if i == 0:
            additionGroups.append([i])
        elif i-1 in multIndex:
            additionGroups[-1].append(i)
        else:
            additionGroups.append([i])


    for group in additionGroups:
        runSum = 1
        for idx in group:
            runSum = digits[idx]*runSum
        check += runSum


    return check == rst
    

with open("input.txt","r") as file:
    rst = []
    digits = []
    for line in file.readlines():
        a,b = line.strip().split(": ")
        rst.append(int(a))
        digits.append([int(digit) for digit in b.split(" ")])

pt1 = 0
pt2 = 0
check = defaultdict(list)
for i in range(len(rst)):

    #permutations is all combinations of 0,1 of locations inbetween numbers
    permutationsPt1 = list(itertools.product(range(2),repeat = len(digits[i])-1))
    permutationsPt2 = list(itertools.product(range(3),repeat = len(digits[i])-1))

    for j in range(len(permutationsPt1)):
        if checkRstPt1(rst[i],digits[i],permutationsPt1[j]):
            pt1+=rst[i]
            break

    for j in range(len(permutationsPt2)):
        if rst[i]==7290 and permutationsPt2[j] == (1,2,1):
            pass

        if checkRstPt2(rst[i],digits[i],permutationsPt2[j]):
            pt2+=rst[i]
            break


print(pt1)
print(pt2)




