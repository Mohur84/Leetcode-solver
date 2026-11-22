class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        queue=deque()
        visited=set()
        have_boxes=set(initialBoxes)
        collected_keys=set()
        for box in initialBoxes:
            if status[box]==1:
                queue.append(box)
        total=0
        while queue:
            box=queue.popleft()
            if box in visited:
                continue
            visited.add(box)
            total+=candies[box]
            for key in keys[box]:
                collected_keys.add(key)
                if key in have_boxes and key not in visited:
                    queue.append(key)
            for new_box in containedBoxes[box]:
                have_boxes.add(new_box)
                if (status[new_box]==1 or new_box in collected_keys):
                    if new_box not in visited:
                        queue.append(new_box)
        return total