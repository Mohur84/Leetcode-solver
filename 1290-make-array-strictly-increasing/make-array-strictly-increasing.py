class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2=sorted(set(arr2))
        dp={-1:0}
        for num in arr1:
            new_dp={}
            for prev, cost in dp.items():
                if num>prev:
                    new_dp[num]=min(
                        new_dp.get(num, float('inf')),
                        cost
                    )
                idx=bisect_right(arr2, prev)
                if idx<len(arr2):
                    replacement=arr2[idx]
                    new_dp[replacement]=min(
                        new_dp.get(replacement, float('inf')),
                        cost+1
                    )
            if not new_dp:
                return -1
            dp=new_dp
        return min(dp.values())