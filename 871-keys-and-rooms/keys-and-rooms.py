class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited=set()
        stack=[0]
        while stack:
            room=stack.pop()
            if room in visited:
                continue
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
        return len(visited)==len(rooms)