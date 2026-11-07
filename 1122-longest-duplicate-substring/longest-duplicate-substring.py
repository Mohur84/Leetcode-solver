class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n=len(s)
        mod=(1<<61)-1
        base=26
        nums=[ord(c)-ord('a') for c in s]
        def search(length):
            if length==0:
                return 0
            power=pow(base, length, mod)
            h=0
            seen=set()
            for i in range(length):
                h=(h*base+nums[i])%mod
            seen.add(h)
            for i in range(length, n):
                h=(h*base-nums[i-length]*power+nums[i])%mod
                if h in seen:
                    return i-length+1
                seen.add(h)
            return -1
        left, right=1, n-1
        start=-1
        best_length=0
        while left<=right:
            mid=(left+right)//2
            index=search(mid)
            if index!=-1:
                start=index
                best_length=mid
                left=mid+1
            else:
                right=mid-1
        if start==-1:
            return ""
        return s[start:start+best_length]