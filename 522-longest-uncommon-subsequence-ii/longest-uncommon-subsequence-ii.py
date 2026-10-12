class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        def is_subsequence(s:str, t:str)->bool:
            i=0
            for ch in t:
                if i<len(s) and s[i]==ch:
                    i+=1
            return i==len(s)
        strs.sort(key=len, reverse=True)
        for i, s in enumerate(strs):
            uncommon=True
            for j, t in enumerate(strs):
                if i!=j and is_subsequence(s, t):
                    uncommon=False
                    break
            if uncommon:
                return len(s)
        return -1