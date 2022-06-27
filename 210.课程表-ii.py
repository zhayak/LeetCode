#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        degrees = [0 for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            degrees[course] += 1
        
        queue = collections.deque()
        ans = []
        for course in range(numCourses):
            if degrees[course] == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            ans.append(course)
            for next_course in graph[course]:
                degrees[next_course] -= 1
                if degrees[next_course] == 0:
                    queue.append(next_course)
        
        return ans if len(ans) == numCourses else []

# @lc code=end

