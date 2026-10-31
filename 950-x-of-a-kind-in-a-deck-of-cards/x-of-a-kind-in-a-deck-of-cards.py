class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        counts=Counter(deck)
        common_gcd=reduce(gcd, counts.values())
        return common_gcd>=2