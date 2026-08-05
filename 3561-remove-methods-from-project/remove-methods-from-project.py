from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)
        
        # Step 1: find all methods reachable from k (suspicious set)
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)
        while queue:
            node = queue.popleft()
            for nxt in graph[node]:
                if nxt not in suspicious:
                    suspicious.add(nxt)
                    queue.append(nxt)
        
        # Step 2: check if any non-suspicious method invokes a suspicious one
        for a, b in invocations:
            if b in suspicious and a not in suspicious:
                return list(range(n))  # can't remove — return everything
        
        # Step 3: return all non-suspicious methods
        return [i for i in range(n) if i not in suspicious]