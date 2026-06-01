class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s : 
            if x =="[" or x =="{" or x == "(": 
             stack.append(x)
            else: 
                if len(stack) == 0 : 
                    return False
                top = stack.pop()
                if top == "[" and x!="]" : 
                    return False
                if top == "{" and x!="}" : 
                    return False
                if top == "(" and x!=")" : 
                    return False
        return len(stack) == 0 


