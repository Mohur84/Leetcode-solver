class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        s=list(target)
        m=len(stamp)
        n=len(target)
        result=[]
        visited=[False]*(n-m+1)
        def can_replace(pos):
            changed=False
            for i in range(m):
                if s[pos+i]=='?':
                    continue
                if s[pos+i]!=stamp[i]:
                    return False
                changed=True
            return changed
        def replace(pos):
            for i in range(m):
                s[pos+i]='?'
        while '?'*n!=''.join(s):
            progress=False
            for i in range(n-m+1):
                if not visited[i] and can_replace(i):
                    replace(i)
                    visited[i]=True
                    result.append(i)
                    progress=True
            if not progress:
                return []
        return result[::-1]