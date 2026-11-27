class Solution:
    def sortString(self, s: str) -> str:
        count=[0]*26
        for ch in s:
            count[ord(ch)-ord('a')]+=1
        result=[]
        while len(result)<len(s):
            for i in range(26):
                if count[i]>0:
                    result.append(chr(i+ord('a')))
                    count[i]-=1
            for i in range(25, -1, -1):
                if count[i]>0:
                    result.append(chr(i+ord('a')))
                    count[i]-=1
        return ''.join(result)