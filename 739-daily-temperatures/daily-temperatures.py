class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        answer=[0]*n
        stack=[]
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                prev=stack.pop()
                answer[prev]=i-prev
            stack.append(i)
        return answer