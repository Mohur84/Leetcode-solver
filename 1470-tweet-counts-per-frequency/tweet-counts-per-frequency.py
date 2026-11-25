class TweetCounts:
    def __init__(self):
        self.tweets=defaultdict(list)
    def recordTweet(self, tweetName: str, time: int) -> None:
        insort(self.tweets[tweetName], time)
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> list[int]:
        intervals={
            "minute":60,
            "hour":3600,
            "day":86400
        }
        interval=intervals[freq]
        size=(endTime-startTime)//interval+1
        result=[0]*size
        times=self.tweets[tweetName]
        left=bisect_left(times, startTime)
        right=bisect_right(times, endTime)
        for i in range(left, right):
            index=(times[i]-startTime)//interval
            result[index]+=1
        return result