class Solution:
    def maxAbsValExpr(self, arr1: list[int], arr2: list[int]) -> int:
        max_values=[float('-inf')]*4
        min_values=[float('inf')]*4
        for i in range(len(arr1)):
            a=arr1[i]
            b=arr2[i]
            values=[
                a+b+i,
                a+b-i,
                a-b+i,
                a-b-i
            ]
            for k in range(4):
                max_values[k]=max(max_values[k], values[k])
                min_values[k]=min(min_values[k], values[k])
        answer=0
        for k in range(4):
            answer=max(answer, max_values[k]-min_values[k])
        return answer