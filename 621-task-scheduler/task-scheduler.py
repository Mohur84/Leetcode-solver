class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq=Counter(tasks)
        max_freq=max(freq.values())
        count_max=sum(
            1 for count in freq.values()
            if count==max_freq
        )
        return max(
            len(tasks),
            (max_freq-1)*(n+1)+count_max
        )