class TopVotedCandidate:
    def __init__(self, persons: list[int], times: list[int]):
        self.times=times
        self.leaders=[]
        count=defaultdict(int)
        leader=-1
        max_votes=0
        for person in persons:
            count[person]+=1
            if count[person]>=max_votes:
                leader=person
                max_votes=count[person]
            self.leaders.append(leader)
    def q(self, t: int) -> int:
        index=bisect.bisect_right(self.times, t)-1
        return self.leaders[index]