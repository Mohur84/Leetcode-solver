class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        count=Counter(nums)
        values=list(count.keys())
        n=len(nums)
        m=len(values)
        graph=[[] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                total=values[i]+values[j]
                root=isqrt(total)
                if root*root==total:
                    graph[i].append(j)
        @lru_cache(None)
        def dfs(last, remaining):
            if sum(remaining)==0:
                return 1
            result=0
            for nxt in graph[last]:
                if remaining[nxt]>0:
                    updated=list(remaining)
                    updated[nxt]-=1
                    result+=dfs(nxt, tuple(updated))
            return result
        answer=0
        for i in range(m):
            if count[values[i]]>0:
                remaining=[count[v] for v in values]
                remaining[i]-=1
                answer+=dfs(i, tuple(remaining))
        return answer