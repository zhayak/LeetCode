#
# @lc app=leetcode.cn id=1905 lang=python3
#
# [1905] 统计子岛屿
#

# @lc code=start
class Solution:
    def bfs(self, grid1, grid2, node, visited):
        queue = collections.deque([node])
        visited.add(node)
        isSub = grid1[node[0]][node[1]] == 1
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nxt_x = x + dx
                nxt_y = y + dy
                if nxt_x < 0 or nxt_x >= len(grid2) or nxt_y < 0 or nxt_y >= len(grid2[0]) or (nxt_x, nxt_y) in visited or grid2[nxt_x][nxt_y] == 0:
                    continue
                visited.add((nxt_x, nxt_y))
                queue.append((nxt_x, nxt_y))
                if grid1[nxt_x][nxt_y] != 1:
                    isSub = False
        return isSub
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if grid2 is None or len(grid2) == 0:
            return 0
        visited = set()
        cnt = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i, j) not in visited:
                    isSub = self.bfs(grid1, grid2, (i, j), visited)
                    if isSub:
                        cnt += 1
        return cnt

# @lc code=end

