class Solution:
    def freqAlphabets(self, s: str) -> str:
        result=[]
        i=0
        while i<len(s):
            if i+2<len(s) and s[i+2]=='#':
                num=int(s[i:i +2])
                i+=3
            else:
                num=int(s[i])
                i+=1
            result.append(chr(num+96))
        return ''.join(result)