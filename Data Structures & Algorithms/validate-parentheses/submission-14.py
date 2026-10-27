class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s_map = {"]" : "[" , "}": "{" , ")" : "(" } 
        for x in s : 
            if x in s_map: 
                if stack and stack[-1] == s_map[x]: 
                    stack.pop()
                else: 
                    return False 
            else: 
                stack.append(x)
        return len(stack) == 0 

        