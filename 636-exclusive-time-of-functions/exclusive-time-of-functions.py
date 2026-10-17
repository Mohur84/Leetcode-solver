class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        result=[0]*n
        stack=[]
        prev_time=0
        for log in logs:
            func_id, event, timestamp=log.split(":")
            func_id=int(func_id)
            timestamp=int(timestamp)
            if event=="start":
                if stack:
                    result[stack[-1]]+=timestamp-prev_time
                stack.append(func_id)
                prev_time=timestamp
            else:
                result[stack.pop()]+=timestamp-prev_time+1
                prev_time=timestamp+1
        return result