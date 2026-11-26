class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        teams=votes[0]
        n=len(teams)
        count={team:[0]*n for team in teams}
        for vote in votes:
            for i, team in enumerate(vote):
                count[team][i]+=1
        result=sorted(
            teams,
            key=lambda team:([-x for x in count[team]], team)
        )
        return ''.join(result)