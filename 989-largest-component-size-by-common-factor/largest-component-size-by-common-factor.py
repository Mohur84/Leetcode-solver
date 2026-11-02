class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        n=len(nums)
        parent=list(range(n))
        size=[1]*n
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x, y):
            root_x=find(x)
            root_y=find(y)
            if root_x==root_y:
                return
            if size[root_x]<size[root_y]:
                root_x, root_y=root_y, root_x
            parent[root_y]=root_x
            size[root_x]+=size[root_y]
        factor_owner={}
        for i, num in enumerate(nums):
            x=num
            factor=2
            while factor*factor<=x:
                if x%factor==0:
                    if factor in factor_owner:
                        union(i, factor_owner[factor])
                    else:
                        factor_owner[factor]=i
                    while x%factor==0:
                        x//=factor
                factor+=1
            if x>1:
                if x in factor_owner:
                    union(i, factor_owner[x])
                else:
                    factor_owner[x]=i
        return max(size[find(i)] for i in range(n))