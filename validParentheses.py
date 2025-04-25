def isValid(s: str) -> bool:
    bracketStack = []

    if len(s) == 0 or len(s) == 1 or s[0] == ')' or s[0] == ']' or s[0] == '}':
        return False

    for c in s:
        if c == '(' or c == '[' or c ==  '{':
            bracketStack += c
        else:
            if len(bracketStack) != 0:
                if c == ')' and bracketStack[-1] == '(':
                    bracketStack.pop()
                elif c == ']' and bracketStack[-1] == '[':
                    bracketStack.pop()
                elif c == '}' and bracketStack[-1] == '{':
                    bracketStack.pop()
                else:
                    return False
            else:
                return False
    
    if len(bracketStack) != 0:
        return False
    
    return True

s = '(]'
print(isValid(s))