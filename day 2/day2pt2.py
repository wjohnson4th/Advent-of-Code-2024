



#check if reactor report is safe
#allowed 1 fault via removing a number from a report
#final answer is determining how many of the reports are safe
#inputs are all positive intergers

#define check safe used to check if list of ints is ok 
def check_safe(report:list[int]) ->int:
    """Checks whether input list is considered safe
    """
    allowableDiff = [1,2,3] #numbers must be different by values in this list
    safe = 1 #create flag variable assuming safe that will be set to zero if unsafe
    delta = 0 #create variable that tracks the first sign of difference
    diffs = [] #for troubleshooting

    #list of indexes where a fault occured between two index 
    #if list contains more than 2 entries, not safe
    #if there isn't a common number in the two entries then you would need to remove more than one index meaning not safe
    faults = [] # [[1,2],[2,3]] one fault, safe

    #loop going through report and determining fault cases
    for i in range(len(report)-1):

        diff = report[i+1]-report[i] #get diff
        diffs.append(diff)
        sign = (diff>0)-(diff<0) #get sign of diff

        #perform sign logic of increasing/decreasing check
        if i == 0: #set delta based on initial sign 
            delta = sign
        else:
            if sign!=delta:
                safe = 0
                faults.append([i,i+1])

        #check change logic
        if abs(diff) not in allowableDiff:
            safe = 0
            faults.append([i,i+1])

    return safe,diffs,faults
        



#actual input
with open("input.txt","r") as file:
    content = file.readlines()

#grab each line and append them to the report list
reports = []
for line in content:
    lines = line.strip().split(" ") #get list of just nums
    lines = [int(num) for num in lines] #convert nums from string to int
    reports.append(lines)



#test input
#reports = [[48, 51, 52, 55, 58, 61, 58, 57]]


safeReports = 0 #running sum of number of safe reports
for report in reports:
   
    safe,diffs,faults = check_safe(report)

    #false positives to check 

    #check if ends are removed what happens?
    if safe == 0:
        #checks if safe if one of the end values are revmoed
        safe = (check_safe(report[1:])[0]>0) or (check_safe(report[:-1])[0]>0)

    #check if only a signle fault occurs
    if safe == 0:
        if len(faults)==1:
            tempSafe = 0
            #slice array twice for each of the two numbers where the fault was detected
            #check if that list is safe if you were to remove one of the two numbers in question
            for fault in faults[0]: #grab only detected fault
                idx = fault
                check = report[:idx]+report[idx+1:]
                tempSafe = max(tempSafe,check_safe(check)[0])
            safe = tempSafe
    
    #check if a single fault occurs that if removed would cause system to work
    if safe == 0:
        if len(faults)==2:
            if faults[0][1] == faults[1][0]:
                #check if removing common value makes safe
                safe = check_safe(report[:faults[0][1]]+report[faults[0][1]+1:])[0] #check sliced list

    #trouble shooting
    if safe==True: #len(faults)>0 and
        print(f"entries: {report},diffs: {diffs}, faults:{faults}, safe:{safe}")

    #add safe to safe report var
    safeReports += safe

print(f"number of safe reports pt1: {safeReports}")



        







