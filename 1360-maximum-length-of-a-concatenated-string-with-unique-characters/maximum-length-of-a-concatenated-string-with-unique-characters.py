class Solution:
    def maxLength(self, arr: list[str]) -> int:
        masks=[]
        for word in arr:
            mask=0
            valid=True
            for ch in word:
                bit=1<<(ord(ch)-ord('a'))
                if mask & bit:
                    valid=False
                    break
                mask |= bit
            if valid:
                masks.append((mask, len(word)))
        dp=[(0, 0)]
        for mask, length in masks:
            new_states=[]
            for used_mask, total_length in dp:
                if used_mask & mask==0:
                    new_states.append(
                        (used_mask | mask, total_length+length)
                    )
            dp.extend(new_states)
        return max(length for mask, length in dp)