class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        n=len(s)
        parent=list(range(n))
        rank=[0]*n
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x, y):
            root_x=find(x)
            root_y=find(y)
            if root_x==root_y:
                return
            if rank[root_x]<rank[root_y]:
                parent[root_x]=root_y
            elif rank[root_x]>rank[root_y]:
                parent[root_y]=root_x
            else:
                parent[root_y]=root_x
                rank[root_x]+=1
        for a, b in pairs:
            union(a, b)
        from collections import defaultdict
        groups=defaultdict(list)
        for i in range(n):
            groups[find(i)].append(s[i])
        for group in groups.values():
            group.sort(reverse=True)
        result=[]
        for i in range(n):
            root=find(i)
            result.append(groups[root].pop())
        return "".join(result)