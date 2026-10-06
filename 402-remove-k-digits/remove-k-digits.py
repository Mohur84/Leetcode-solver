class Solution:
    def removeKdigits(self, num, k):
        stack=[]
        for digit in num:
            while k>0 and stack and stack[-1]>digit:
                stack.pop()
                k-=1
            stack.append(digit)
        if k>0:
            stack=stack[:-k]
        result=''.join(stack).lstrip('0')
        return result if result else '0'