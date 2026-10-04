class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights=[h for w, h in envelopes]
        tails=[]
        for h in heights:
            left=0
            right=len(tails)
            while left<right:
                mid=(left+right)//2
                if tails[mid]<h:
                    left=mid+1
                else:
                    right=mid
            if left==len(tails):
                tails.append(h)
            else:
                tails[left]=h
        return len(tails)