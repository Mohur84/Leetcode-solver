class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        result=[]
        n=len(arr)
        for size in range(n, 1, -1):
            max_index=arr.index(size)
            if max_index==size-1:
                continue
            if max_index!=0:
                arr[:max_index+1]=reversed(arr[:max_index+1])
                result.append(max_index+1)
            arr[:size]=reversed(arr[:size])
            result.append(size)
        return result