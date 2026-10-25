class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        possible_sizes=[
            k for k in range(1, n//2+1)
            if total*k%n==0
        ]
        if not possible_sizes:
            return False
        max_size=max(possible_sizes)
        dp=[set() for _ in range(max_size+1)]
        dp[0].add(0)
        for num in nums:
            for size in range(max_size, 0, -1):
                for prev_sum in dp[size - 1]:
                    dp[size].add(prev_sum + num)
        for k in possible_sizes:
            if (total * k) // n in dp[k]:
                return True
        return False