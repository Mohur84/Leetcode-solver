class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for ch in s:
            if ch=='(':
                stack.append(0)
            else:
                inner=stack.pop()
                score=max(2*inner, 1)
                stack[-1]+=score
        return stack[0]