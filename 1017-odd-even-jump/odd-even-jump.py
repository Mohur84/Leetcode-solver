class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        n=len(arr)
        next_higher=[0]*n
        next_lower=[0]*n
        stack=[]
        for i in sorted(range(n), key=lambda i: (arr[i], i)):
            while stack and i>stack[-1]:
                next_higher[stack.pop()]=i
            stack.append(i)
        stack=[]
        for i in sorted(range(n), key=lambda i:(-arr[i], i)):
            while stack and i>stack[-1]:
                next_lower[stack.pop()]=i
            stack.append(i)
        odd=[False]*n
        even=[False]*n
        odd[-1]=True
        even[-1]=True
        for i in range(n-2, -1, -1):
            odd[i]=even[next_higher[i]]
            even[i]=odd[next_lower[i]]
        return sum(odd)