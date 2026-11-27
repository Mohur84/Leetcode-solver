class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen={0: -1}
        mask=0
        result=0
        vowels={
            'a':0,
            'e':1,
            'i':2,
            'o':3,
            'u':4
        }
        for i, ch in enumerate(s):
            if ch in vowels:
                mask^=(1<<vowels[ch])
            if mask in seen:
                result=max(result, i-seen[mask])
            else:
                seen[mask]=i
        return result