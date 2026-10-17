class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])
        max_heap=[]
        total_time=0
        for duration, deadline in courses:
            total_time+=duration
            heapq.heappush(max_heap, -duration)
            if total_time>deadline:
                longest=-heapq.heappop(max_heap)
                total_time-=longest
        return len(max_heap)