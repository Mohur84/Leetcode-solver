class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n=len(arr)
        queue=deque([start])
        visited={start}
        while queue:
            i=queue.popleft()
            if arr[i]==0:
                return True
            for next_index in (i+arr[i], i-arr[i]):
                if 0<=next_index<n and next_index not in visited:
                    visited.add(next_index)
                    queue.append(next_index)
        return False