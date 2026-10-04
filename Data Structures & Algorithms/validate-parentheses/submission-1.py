class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        
        pairs = {')': '(', '}': '{', ']': '['}

        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in ")}]":
                if not stack:
                    return False
                if stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False

        

