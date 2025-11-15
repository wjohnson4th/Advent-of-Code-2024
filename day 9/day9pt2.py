

with open("input.txt","r") as file:
    myInput = file.readline().strip().split()
    myInput = list(map(int,*myInput))

#print(myInput)

mem = []

#starting idx and size of file 
files = [] #list containing [id,idx,size]
#starting idx and size of empty spot
blanks = [] #list containing [idx,size]
id = 0
for i in range(len(myInput)):
    if i%2==0:
        files.append([id,len(mem),myInput[i]])
        mem = mem + [id]*myInput[i]
        id += 1
    else:
        blanks.append([len(mem),myInput[i]])
        mem = mem + [None]*myInput[i]
        
#go backwards in files list trying to find smallest location in blanks list to place in mem


back = len(files)-1

while True:
    for front in range(len(blanks)):
        #if you can move a backward mem forward update mem and update blanks
        if (blanks[front][1] >= files[back][2]) and (blanks[front][0]<files[back][1]):
            #print(mem)
            #update in memory of new id locations
            for i in range(blanks[front][0],blanks[front][0]+files[back][2]):
                mem[i] = files[back][0]

            #update old mem locations with None
            for i in range(files[back][1],files[back][1]+files[back][2]):
                mem[i] = None
            
            #update blanks
            blanks[front][0] = blanks[front][0] + files[back][2]
            blanks[front][1] = blanks[front][1] - files[back][2]
            
            #break out of loop and start over from front of blanks
            break
    
    # if you get here you haven't found a suitable position for the back element
    #first check whether back == 0 to break out of while loop
    #if not zero just decrement
    if back == 0:
        break
    else:
        back-=1

#print(mem)


pt2 = 0
for i,val in enumerate(mem):
    if val==None:
        continue
    pt2+= i*val

print(pt2)


