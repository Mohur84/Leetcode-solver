class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        stack=[float('inf')]
        result=0
        for num in arr:
            while stack[-1]<=num:
                mid=stack.pop()
                result+=mid*min(stack[-1], num)
            stack.append(num)
        while len(stack)>2:
            result+=stack.pop()*stack[-1]
        return result