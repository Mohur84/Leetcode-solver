class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        n=len(req_skills)
        skill_index={
            skill: i for i, skill in enumerate(req_skills)
        }
        full_mask=(1<<n)-1
        people_masks=[]
        for person in people:
            mask=0
            for skill in person:
                mask |= 1<<skill_index[skill]
            people_masks.append(mask)
        dp={0:[]}
        for i, person_mask in enumerate(people_masks):
            new_dp=dp.copy()
            for mask, team in dp.items():
                new_mask=mask | person_mask
                if new_mask not in new_dp or len(new_dp[new_mask])>len(team)+1:
                    new_dp[new_mask]=team+[i]
            dp=new_dp
        return dp[full_mask]