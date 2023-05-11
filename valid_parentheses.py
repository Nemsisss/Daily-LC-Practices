#valid parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                elif (i==']' and stack[len(stack)-1]!='[') or (i=='}' and stack[len(stack)-1]!='{') or (i==')' and stack[len(stack)-1]!='('):
                    return False
                stack.pop()
        
        return not len(stack)
