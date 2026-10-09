class Solution:
    def repeatedSubstringPattern(self, s):
        doubled=(s+s)[1:-1]
        return s in doubled