class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        def dfs(nums):
            if len(nums)==1:
                return abs(nums[0]-24)<1e-6
            n=len(nums)
            for i in range(n):
                for j in range(i+1, n):
                    a, b=nums[i], nums[j]
                    remaining=[
                        nums[k] for k in range(n)
                        if k!=i and k!=j
                    ]
                    results=[
                        a+b,
                        a-b,
                        b-a,
                        a*b
                    ]
                    if abs(b)>1e-6:
                        results.append(a/b)
                    if abs(a)>1e-6:
                        results.append(b/a)
                    for value in results:
                        if dfs(remaining+[value]):
                            return True
            return False
        return dfs(cards)