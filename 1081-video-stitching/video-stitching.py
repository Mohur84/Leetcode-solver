class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        clips.sort()
        current_end=0
        farthest=0
        count=0
        i=0
        n=len(clips)
        while current_end<time:
            while i<n and clips[i][0]<=current_end:
                farthest=max(farthest, clips[i][1])
                i+=1
            if farthest==current_end:
                return -1
            count+=1
            current_end=farthest
        return count