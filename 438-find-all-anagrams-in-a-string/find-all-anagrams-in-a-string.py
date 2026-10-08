class Solution:
    def findAnagrams(self, s, p):
        if len(p)>len(s):
            return []
        need=Counter(p)
        window=Counter()
        result=[]
        left=0
        for right in range(len(s)):
            window[s[right]]+=1
            if right-left+1>len(p):
                window[s[left]]-=1
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1
            if window==need:
                result.append(left)
        return result