class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            stack.append(ch)
            if len(stack)>=3 and stack[-3:]==['a','b','c']:
                stack.pop()
                stack.pop()
                stack.pop()
        return len(stack)==0