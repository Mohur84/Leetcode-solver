class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length=0
        for ch in s:
            if ch.isdigit():
                length*=int(ch)
            else:
                length+=1
        for ch in reversed(s):
            k%=length
            if ch.isdigit():
                length//=int(ch)
            else:
                if k==0:
                    return ch
                length-=1
        return ""