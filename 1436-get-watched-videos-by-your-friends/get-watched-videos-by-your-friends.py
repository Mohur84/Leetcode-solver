class Solution:
    def watchedVideosByFriends(self, watchedVideos: list[list[str]], friends: list[list[int]], id: int, level: int) -> list[str]:
        queue=deque([id])
        visited={id}
        current_level=0
        while queue and current_level<level:
            for _ in range(len(queue)):
                person=queue.popleft()
                for friend in friends[person]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)
            current_level+=1
        video_count=Counter()
        for person in queue:
            video_count.update(watchedVideos[person])
        result=sorted(
            video_count.keys(),
            key=lambda video:(video_count[video], video)
        )
        return result