class Solution:
    def canConstruct(self, ransomNote, magazine):
        available=Counter(magazine)
        for ch in ransomNote:
            if available[ch]==0:
                return False
            available[ch]-=1
        return True