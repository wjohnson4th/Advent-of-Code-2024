
with open("input.txt","r") as file:
    myInput = file.readline().strip().split()
    myInput = list(map(int,*myInput))

print(myInput)

mem = []

id = 0
for i in range(len(myInput)):
    if i%2==0:
        mem = mem + [id]*myInput[i]
        id += 1
    else:
        mem = mem + [None]*myInput[i]
    
#two pointer walk down
front = 0
back = len(mem)-1

while True:
    while mem[back]==None:
        back-=1

    #set front to None space
    while mem[front]!=None:
        front+=1
    
    if front>=back:
        break

    #once front and back are set to a None space and a number space, swap them
    mem[front]=mem[back]
    mem[back]=None


pt1 = 0
for i,val in enumerate(mem):
    if val==None:
        break
    pt1+= i*val

print(pt1)


