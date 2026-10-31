class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars=list(s)
        left=0
        right=len(chars)-1
        while left<right:
            if not chars[left].isalpha():
                left+=1
            elif not chars[right].isalpha():
                right-=1
            else:
                chars[left], chars[right]=chars[right], chars[left]
                left+=1
                right-=1
        return ''.join(chars)