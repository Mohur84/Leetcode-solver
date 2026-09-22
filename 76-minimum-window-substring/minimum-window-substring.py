from collections import Counter
class Solution:
    def minWindow(self, s:str, t:str)->str:
        if not s or not t:
            return ""
        need=Counter(t)
        missing=len(t)
        left=start=end=0
        for right in range(1, len(s)+1):
            ch=s[right-1]
            if need[ch]>0:
                missing-=1
            need[ch]-=1
            while missing==0:
                if end==0 or right - left < end - start:
                    start, end = left, right
                need[s[left]]+=1
                if need[s[left]]>0:
                    missing+=1
                left+=1
        return s[start:end]
