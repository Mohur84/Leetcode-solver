class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        result=""
        for p in permutations(arr):
            hours=p[0]*10+p[1]
            minutes=p[2]*10+p[3]
            if hours<24 and minutes<60:
                time=f"{hours:02d}:{minutes:02d}"
                if time>result:
                    result=time
        return result