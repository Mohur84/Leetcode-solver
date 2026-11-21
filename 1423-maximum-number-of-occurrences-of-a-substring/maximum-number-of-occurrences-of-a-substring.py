class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count=Counter()
        for i in range(len(s)-minSize+1):
            sub=s[i:i+minSize]
            if len(set(sub))<=maxLetters:
                count[sub]+=1
        return max(count.values(), default=0)