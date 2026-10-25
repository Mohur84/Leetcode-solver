class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines=1
        current_width=0
        for ch in s:
            width=widths[ord(ch)-ord('a')]
            if current_width + width>100:
                lines+=1
                current_width=width
            else:
                current_width+=width
        return [lines, current_width]