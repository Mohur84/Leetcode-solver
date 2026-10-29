class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        groups=set()
        for word in words:
            even_chars=sorted(word[::2])
            odd_chars=sorted(word[1::2])
            signature=(tuple(even_chars), tuple(odd_chars))
            groups.add(signature)
        return len(groups)