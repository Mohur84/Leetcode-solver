class Solution:
    def canCross(self, stones):
        n=len(stones)
        if n<2 or stones[1]!=1:
            return False
        stone_set=set(stones)
        memo={}
        def dfs(position, jump):
            if position==stones[-1]:
                return True
            key=(position, jump)
            if key in memo:
                return memo[key]
            for next_jump in (jump-1, jump, jump+1):
                if next_jump<=0:
                    continue
                next_position=position+next_jump
                if next_position in stone_set:
                    if dfs(next_position, next_jump):
                        memo[key]=True
                        return True
            memo[key]=False
            return False
        return dfs(1, 1)