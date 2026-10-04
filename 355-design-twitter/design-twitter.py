import heapq
class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}
    def postTweet(self, userId, tweetId):
        self.time += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        if userId not in self.following:
            self.following[userId] = set()
    def getNewsFeed(self, userId):
        heap = []
        users = self.following.get(userId, set()).copy()
        users.add(userId)
        for uid in users:
            if uid in self.tweets and self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]
                heapq.heappush(
                    heap,
                    (-time, tweetId, uid, index)
                )
        result = []
        while heap and len(result) < 10:
            neg_time, tweetId, uid, index = heapq.heappop(heap)
            result.append(tweetId)
            index -= 1
            if index >= 0:
                time, tweetId = self.tweets[uid][index]
                heapq.heappush(
                    heap,
                    (-time, tweetId, uid, index)
                )
        return result
    def follow(self, followerId, followeeId):
        if followerId == followeeId:
            return
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
    def unfollow(self, followerId, followeeId):
        if followerId in self.following:
            self.following[followerId].discard(followeeId)