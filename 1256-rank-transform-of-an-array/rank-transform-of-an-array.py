class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_arr=sorted(set(arr))
        rank={}
        for i, num in enumerate(sorted_arr):
            rank[num]=i+1
        result=[]
        for num in arr:
            result.append(rank[num])
        return result