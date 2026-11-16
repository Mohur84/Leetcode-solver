from collections import defaultdict, deque
class Solution:
    def sortItems(self, n, m, group, beforeItems):
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        item_graph = defaultdict(list)
        group_graph = defaultdict(list)
        item_indegree = [0] * n
        group_indegree = [0] * m
        for v in range(n):
            for u in beforeItems[v]:
                item_graph[u].append(v)
                item_indegree[v] += 1
                if group[u] != group[v]:
                    group_graph[group[u]].append(group[v])
                    group_indegree[group[v]] += 1
        def topo_sort(graph, indegree, size):
            queue = deque(
                i for i in range(size) if indegree[i] == 0
            )
            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            return order if len(order) == size else []
        group_order = topo_sort(
            group_graph, group_indegree, m
        )
        if not group_order:
            return []
        item_order = topo_sort(
            item_graph, item_indegree, n
        )
        if not item_order:
            return []
        grouped_items = defaultdict(list)
        for item in item_order:
            grouped_items[group[item]].append(item)
        result = []
        for g in group_order:
            result.extend(grouped_items[g])
        return result