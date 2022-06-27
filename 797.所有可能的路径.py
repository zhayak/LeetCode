#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def dfs(self, graph, curr_node, path, paths):
        if curr_node == len(graph) - 1:
            paths.append(path[:])
            return
        for next_node in graph[curr_node]:
            path.append(next_node)
            self.dfs(graph, next_node, path, paths)
            path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        self.dfs(graph, 0, [0], paths)
        return paths
# @lc code=end

