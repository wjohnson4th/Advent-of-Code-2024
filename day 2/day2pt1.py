

#check if reactor report is safe
#final answer is determining how many of the reports are safe
#inputs are all positive intergers

allowableDiff = [1,2,3] #numbers must be different by values in this list

with open("input.txt","r") as file:
    content = file.readlines()

#grab each line and append them to the report list
reports = []
for line in content:
    lines = line.strip().split(" ") #get list of just nums
    lines = [int(num) for num in lines] #convert nums from string to int
    reports.append(lines)

for item in reports:
    print(item)

safeReports = 0 #running sum of number of safe reports
for report in reports:
    safe = 1 #create flag variable assuming safe that will be set to zero if unsafe
    delta = 0 #create variable that tracks the first sign of difference
    diffs = [] #for troubleshooting

    for i in range(len(report)-1):

        diff = report[i+1]-report[i] #get diff
        diffs.append(diff)
        sign = (diff>0)-(diff<0) #get sign of diff

        #perform sign logic of increasing/decreasing check
        if i == 0: #set delta based on initial sign 
            delta = sign
        else:
            if sign!=delta:
                safe = 0 #report not safe since increasing/decreasing switched changed

        #check change logic
        if abs(diff) not in allowableDiff:
            safe = 0

    #add safe to safe report var
    safeReports += safe

print(f"number of safe reports pt1: {safeReports}")



        







