#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        degrees = [0 for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            degrees[course] += 1
        
        queue = collections.deque()
        cnt = 0
        for course in range(numCourses):
            if degrees[course] == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            cnt += 1
            for next_course in graph[course]:
                degrees[next_course] -= 1
                if degrees[next_course] == 0:
                    queue.append(next_course)
        
        return cnt == numCourses

# @lc code=end

