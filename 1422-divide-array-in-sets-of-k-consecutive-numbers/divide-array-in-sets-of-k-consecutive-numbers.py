class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False
        count=Counter(nums)
        for num in sorted(count):
            freq=count[num]
            if freq>0:
                for x in range(num, num+k):
                    if count[x]<freq:
                        return False
                    count[x]-=freq
        return True