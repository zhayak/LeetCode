#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#

# @lc code=start
class Solution:
    def bfs(self, grid, node, visited):
        queue = collections.deque([node])
        visited.add(node)
        while queue:
            x, y = queue.popleft()
            for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                nxt_x = x + dx
                nxt_y = y + dy
                if nxt_x < 0 or nxt_x >= len(grid) or nxt_y < 0 or nxt_y >= len(grid[0]) or (nxt_x, nxt_y) in visited or grid[nxt_x][nxt_y] == 0:
                    continue
                visited.add((nxt_x, nxt_y))
                queue.append((nxt_x, nxt_y))
    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        visited = set()
        cnt = 0
        m, n = len(grid), len(grid[0])
        for j in range(n):
            if grid[0][j] == 1 and (0, j) not in visited:
                self.bfs(grid, (0, j), visited)
            if grid[m - 1][j] == 1 and (m - 1, j) not in visited:
                self.bfs(grid, (m - 1, j), visited)
        for i in range(m):
            if grid[i][0] == 1 and (i, 0) not in visited:
                self.bfs(grid, (i, 0), visited)
            if grid[i][n - 1] == 1 and (i, n - 1) not in visited:
                self.bfs(grid, (i, n - 1), visited)
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    cnt += 1
        return cnt

# @lc code=end

