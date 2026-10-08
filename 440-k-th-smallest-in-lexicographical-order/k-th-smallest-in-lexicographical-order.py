class Solution:
    def findKthNumber(self, n, k):
        def count_steps(prefix):
            steps=0
            first=prefix
            last=prefix
            while first<=n:
                steps+=min(n+1, last+1)-first
                first*=10
                last=last*10+9
            return steps
        curr=1
        k-=1
        while k>0:
            steps=count_steps(curr)
            if steps<=k:
                curr+=1
                k-=steps
            else:
                curr*=10
                k-=1
        return curr