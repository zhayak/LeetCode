#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def bfs(self, grid, node, visited):
        cnt = 1
        queue = collections.deque([node])
        visited.add(node)
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nxt_x = x + dx
                nxt_y = y + dy
                if nxt_x < 0 or nxt_x >= len(grid) or nxt_y < 0 or nxt_y >= len(grid[0]) or grid[nxt_x][nxt_y] == 0 or (nxt_x, nxt_y) in visited:
                    continue
                visited.add((nxt_x, nxt_y))
                queue.append((nxt_x, nxt_y))
                cnt += 1
        return cnt
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        
        visited = set()
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = self.bfs(grid, (i, j), visited)
                    ans = max(ans, area)
        return ans

# @lc code=end

