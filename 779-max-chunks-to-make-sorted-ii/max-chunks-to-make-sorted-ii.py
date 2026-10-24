class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        stack=[]
        for num in arr:
            if not stack or num>=stack[-1]:
                stack.append(num)
            else:
                largest=stack.pop()
                while stack and stack[-1]>num:
                    stack.pop()
                stack.append(largest)
        return len(stack)