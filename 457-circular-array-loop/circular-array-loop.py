class Solution:
    def circularArrayLoop(self, nums):
        n=len(nums)
        def next_index(i):
            return (i+nums[i])%n
        for i in range(n):
            if nums[i]==0:
                continue
            direction=nums[i]>0
            slow=fast=i
            while True:
                next_slow=next_index(slow)
                if nums[next_slow]==0 or (nums[next_slow]>0)!=direction:
                    break
                next_fast=next_index(fast)
                if nums[next_fast]==0 or (nums[next_fast]>0)!=direction:
                    break
                next_fast = next_index(next_fast)
                if nums[next_fast] == 0 or (nums[next_fast] > 0) != direction:
                    break
                slow=next_slow
                fast=next_fast
                if slow==fast:
                    if next_index(slow)!=slow:
                        return True
                    break
            j=i
            while nums[j]!=0 and (nums[j]>0)==direction:
                nxt=next_index(j)
                nums[j]=0
                j=nxt
        return False