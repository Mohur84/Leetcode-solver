class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        prefix=[0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        def calculate(L, M):
            best_L=0
            answer=0
            for i in range(L+M, len(nums)+1):
                left_sum=prefix[i-M]-prefix[i-M-L]
                best_L=max(best_L, left_sum)
                right_sum=prefix[i]-prefix[i-M]
                answer=max(answer, best_L+right_sum)
            return answer
        return max(
            calculate(firstLen, secondLen),
            calculate(secondLen, firstLen)
        )