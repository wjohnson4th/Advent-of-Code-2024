import re

with open("input.txt","r") as file:
    content = file.readlines()
    contentString = str()
    for line in content:
        contentString = contentString+line.strip()

#pt1
        
#get valid mults
regex = r"(mul\(\d{1,3},\d{1,3}\))"
valid = re.findall(regex,contentString)

#get result
runSum = 0
for item in valid:
    result = re.findall(r"\d{1,3}",item)

    runSum += int(result[0])*int(result[1])

print(f"pt 1 answer: {runSum}")

#pt2

#get valid mults
regex = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
valid = re.findall(regex,contentString)

on = 1
runSum = 0
for item in valid:

    if item == r"do()":
        on=1
    elif item == r"don't()":
        on=0
    else:
        result = re.findall(r"\d{1,3}",item)
        runSum += on*(int(result[0])*int(result[1]))

print(f"pt 2 answer: {runSum}")

