class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        path=[]
        while label>=1:
            path.append(label)
            level=label.bit_length()
            level_start=1<<(level-1)
            level_end=(1<<level)-1
            label=(level_start+level_end-label)//2
        return path[::-1]