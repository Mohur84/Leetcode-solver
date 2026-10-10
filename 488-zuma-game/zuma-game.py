class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove(s,i):
            if i<0:
                return s
            l,r=i,i
            while l>0 and s[l-1]==s[i]:
                l-=1
            while r+1<len(s) and s[r+1]==s[i]:
                r+=1
            if r-l+1>=3:
                return remove(s[:l]+s[r+1:],l-1)
            return s
        hand=''.join(sorted(hand))
        q=deque([(board,hand,0)])
        vis=set([(board,hand)])
        while q:
            b,h,s=q.popleft()
            for i in range(len(b)+1):
                for j in range(len(h)):
                    if j>0 and h[j]==h[j-1]: #skip duplicates
                        continue
                    if i>0 and b[i-1]==h[j]: #skip insert if left
                        continue
                    pick=False
                    if i<len(b) and b[i]==h[j]:
                        pick=True
                    if 0<i<len(b) and b[i-1]==b[i] and b[i]!=h[j]:
                        pick=True
                    if pick:
                        nb=remove(b[:i]+h[j]+b[i:],i)
                        nh=h[:j]+h[j+1:]
                        if not nb:
                            return s+1
                        if (nb,nh) not in vis:
                            q.append((nb,nh,s+1))
                            vis.add((nb,nh))
        return -1   