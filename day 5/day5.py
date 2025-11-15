

with open("input.txt","r") as file:
    content = file.readlines()

def vectorCheck(update:list,key:dict,ansr:list):

    #if this is the last entry or front of the update, append to front of answer and return final answer
    if len(update)==1:
        ansr.insert(0,update[0])
        return None

    check = update[-1]

    flag=1
    for i in range(len(update)-2,-1,-1):
        # if earlier page is supposed to be infront of the current page, rule is violated
        #revese placement and re-run function
        try:
            if update[i] in key[check]:
                value = update.pop(i)
                update.append(value)
                flag = 0
                break
        except:
            pass 
    
    # all rules followed between current check and all values in front of it,
    #append check to front of answer
    #run function again using left of check as update
    if flag==1:
        ansr.insert(0,check)
        vectorCheck(update[:-1],key,ansr)
    else:
        vectorCheck(update,key,ansr)

#seperate rules and udates
idx = content.index("\n")
rulesTxt = content[:idx]
updatesTxt = content[idx+1:]

rules:dict[int:set[int]] = {}
for line in rulesTxt:
    pre,post = line.strip().split("|")
    pre,post = int(pre),int(post)
    if pre not in rules:
        rules[pre] = {post}
    else:
        rules[pre].add(post)

updates = []
for line in updatesTxt:
    updates.append([int(item) for item in line.strip().split(",")])

pt1count = 0
pt2count = 0

ans = []
for update in updates:
    ansr = []
    vectorCheck([*update],rules,ansr)
    if ansr == update:
        pt1count += ansr[int(len(update)/2)]
    else:
        pt2count += ansr[int(len(update)/2)]
    ans.append(ansr)

print(ans)
print(f"pt1 count: {pt1count}")
print(f"pt2 count: {pt2count}")