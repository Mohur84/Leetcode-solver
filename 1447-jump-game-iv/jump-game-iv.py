class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n=len(arr)
        if n==1:
            return 0
        graph=defaultdict(list)
        for i, num in enumerate(arr):
            graph[num].append(i)
        queue=deque([(0, 0)])
        visited={0}
        while queue:
            index, steps=queue.popleft()
            if index==n-1:
                return steps
            for next_index in (index-1, index+1):
                if 0<=next_index<n and next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, steps+1))
            value=arr[index]
            for next_index in graph[value]:
                if next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, steps+1))
            graph[value].clear()
        return -1