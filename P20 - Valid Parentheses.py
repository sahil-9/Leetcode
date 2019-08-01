#Question Link - https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return True
        
        stack, bracket_hash = [], {"(":")", "[":"]", "{":"}"}
        
	   for item in s:
            if item in bracket_hash:
                stack.append(bracket_hash[item])
            elif not stack or stack.pop() != item: 
                return False
        return len(stack) == 0