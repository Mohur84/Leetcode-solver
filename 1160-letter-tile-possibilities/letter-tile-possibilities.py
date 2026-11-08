class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq=Counter(tiles)
        def backtrack():
            count=0
            for ch in freq:
                if freq[ch]>0:
                    freq[ch]-=1
                    count+=1
                    count+=backtrack()
                    freq[ch]+=1
            return count
        return backtrack()