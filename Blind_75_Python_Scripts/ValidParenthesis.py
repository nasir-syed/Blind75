def isValid(s):
    stack = []

    closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

    for c in s:
        if c in closeToOpen: # every key is a closing bracket,
            if stack and stack[-1] == closeToOpen[c]: # stack not empty, and the opening brace is in stack (it should always be at the top of the stack)
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False


brc = "(){}[]"
print(isValid(brc)) # each one is a pair,, opens and closes right after

s = "(){[}]"
print(isValid(s))

