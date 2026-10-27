class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        chars=list(s)
        shift=0
        for i in range(len(s)-1, -1, -1):
            shift=(shift+shifts[i])%26
            chars[i]=chr(
                (ord(s[i])-ord('a')+shift)%26+ord('a')
            )
        return ''.join(chars)