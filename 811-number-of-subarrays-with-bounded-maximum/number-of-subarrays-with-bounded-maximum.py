class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        count=0
        result=0
        for num in nums:
            if num>right:
                count=0
            else:
                count+=1
            result+=count
        count=0
        for num in nums:
            if num>=left:
                count=0
            else:
                count+=1
        def count_at_most(bound):
            current=total=0
            for num in nums:
                if num<=bound:
                    current+=1
                else:
                    current=0
                total+=current
            return total
        return count_at_most(right)-count_at_most(left-1)