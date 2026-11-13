class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        no_delete=arr[0]
        one_delete=float('-inf')
        result=arr[0]
        for i in range(1, len(arr)):
            x=arr[i]
            one_delete=max(no_delete, one_delete+x)
            no_delete=max(x, no_delete+x)
            result=max(result, no_delete, one_delete)
        return result