
#read in text file input from folder directory

with open("input.txt","r") as file:
    content = file.readlines() #gets list of lines as strings

#create two seperate lists for sorting 
list1=[] #left list
list2=[] #right list

#get contents out of lists
for line in content:
   #split up numbers
   num1, num2 = line.split("   ")
   
   #convert nums to ints
   num1 = int(num1)
   num2  = int(num2.strip()) #get's rid of new line 

    #append items into lists
   list1.append(num1)
   list2.append(num2)

#sort lists
list1.sort()
list2.sort()

# go through lists and find absolute distance between numbers
runsum = 0
for i in range(len(list1)):
    runsum += abs(list1[i]-list2[i])

print(f"running sum: {runsum}")


#go through list and find how many times each left number appears in the right list and sum the multiplication 
#for each unique num in list 1 perform the following
# sumation of a*b*c
    # a = the unique number in the left list
    # b = number of times that num is in the left list
    # c = number of times that num is in the right list

#create value that will be retunred as answer
simscore = 0

#create list of unique numbers and the frequency at which they appear
set1 = set(list1) #unique numbers in list 1

for a in set1:
    b = list1.count(a)
    c = list2.count(a)

    simscore += a*b*c

print(f"sim score: {simscore}")

