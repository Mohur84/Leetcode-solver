class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack=[]
        j=0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
        return j==len(popped)