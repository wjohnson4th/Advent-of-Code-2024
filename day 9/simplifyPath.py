def simplifyPath( path: str) -> str:

    def dotOp(stack:list):
        #more than two dots is valid name, do nothing
        if "".join(stack[-3:]) == "...":
            return 
        #only two dots, remove dots and previous dir
        elif "".join(stack[-3:]) == r"/..":
            count  = 0
            while count<2 and stack:
                char = stack.pop()
                if char == r"/":
                    count+=1
            if not stack:
                stack.append(r"/")
        #only one dot, remove/.
        elif "".join(stack[-2:]) == r"/.":
            for _ in range(2):
                stack.pop()
            if not stack:
                stack.append(r"/")
        else:
            pass

        return


    stack = []
    n = len(path)

    for i,c in enumerate(path):
        if i == 0:
            if c != r"/":
                stack.append(r"/")
            stack.append(c)
            continue


        #check if previous was dot when c is /
        if stack[-1]=="." and c ==r"/":
            dotOp(stack)

        #check if previous char is / and skip if so
        if c == r"/" and stack[-1]==r"/":
            continue

        #all checks good, append char
        stack.append(c)

    #run dot op last time
    if stack[-1]==".":
        dotOp(stack)

    #remove back / from stack
    if stack[-1]==r"/" and len(stack)>1:
        stack.pop()

    return "".join(stack)


#print(simplifyPath(r"/a//b////c/d//././/.."))
#print(simplifyPath("/."))
#print(simplifyPath("/.."))
print(simplifyPath("/a/../../b/../c//.//"))
print(simplifyPath("/..hidden"))
print(simplifyPath("/hello../world"))