class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        required=[0]*26
        for word in words2:
            freq=Counter(word)
            for char, count in freq.items():
                index=ord(char)-ord('a')
                required[index]=max(required[index], count)
        result=[]
        for word in words1:
            freq=Counter(word)
            if all(
                freq[chr(i+ord('a'))]>=required[i]
                for i in range(26)
            ):
                result.append(word)
        return result