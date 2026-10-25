class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        n=len(nums)
        change=[0]*n
        for i, value in enumerate(nums):
            left=(i-value+1)%n
            change[left]-=1
            change[(i+1)%n]+=1
        score=sum(value<=i for i, value in enumerate(nums))
        best_score=score
        best_rotation=0
        for k in range(1, n):
            score+=change[k]
            if score>best_score:
                best_score=score
                best_rotation=k
        return best_rotation