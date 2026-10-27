class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_valid_index(string, i):
            skip=0
            while i>=0:
                if string[i]=='#':
                    skip+=1
                    i-=1
                elif skip>0:
                    skip-=1
                    i-=1
                else:
                    break
            return i
        i=len(s)-1
        j=len(t)-1
        while i>=0 or j>=0:
            i=next_valid_index(s, i)
            j=next_valid_index(t, j)
            if i<0 and j<0:
                return True
            if i<0 or j<0:
                return False
            if s[i]!=t[j]:
                return False
            i-=1
            j-=1
        return True