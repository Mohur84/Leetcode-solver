class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total=sum(arr)
        if total%3!=0:
            return False
        target=total//3
        current_sum=0
        parts=0
        for i in range(len(arr)-1):
            current_sum+=arr[i]
            if current_sum==target:
                parts+=1
                current_sum=0
                if parts==2:
                    return True
        return False