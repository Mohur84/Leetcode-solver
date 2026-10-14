class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        from collections import Counter
        target=Counter(s1)
        window=Counter(s2[:len(s1)])
        k=len(s1)
        if window==target:
            return True
        for i in range(k, len(s2)):
            window[s2[i]]+=1
            left_char=s2[i-k]
            window[left_char]-=1
            if window[left_char]==0:
                del window[left_char]
            if window==target:
                return True
        return False