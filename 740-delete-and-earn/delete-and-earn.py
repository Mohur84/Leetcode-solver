class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        points=Counter(nums)
        prev=0
        curr=0
        prev_num=-1
        for num in sorted(points):
            gain=num*points[num]
            if num==prev_num+1:
                prev, curr=curr, max(curr, prev+gain)
            else:
                prev, curr=curr, curr+gain
            prev_num=num
        return curr