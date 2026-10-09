class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        max_length=[0]*26
        current_length=0
        for i, char in enumerate(s):
            if i>0 and (
                ord(char)-ord(s[i-1])==1
                or ord(s[i-1])-ord(char)==25
            ):
                current_length+=1
            else:
                current_length=1
            index=ord(char)-ord('a')
            max_length[index]=max(max_length[index], current_length)
        return sum(max_length)