class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        parent=list(range(26))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x, y):
            px=find(x)
            py=find(y)
            if px!=py:
                parent[px]=py
        for eq in equations:
            if eq[1]=='=':
                x=ord(eq[0])-ord('a')
                y=ord(eq[3])-ord('a')
                union(x, y)
        for eq in equations:
            if eq[1]=='!':
                x=ord(eq[0])-ord('a')
                y=ord(eq[3])-ord('a')
                if find(x)==find(y):
                    return False
        return True