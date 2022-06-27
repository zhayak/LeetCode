#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        queue = collections.deque(["0000"])
        visited = set(["0000"])
        step = 0
        while queue:
            sz = len(queue)
            for i in range(sz):
                curr = queue.popleft()
                if curr == target:
                    return step
                for j in range(4):
                    for direction in [-1, 1]:
                        nxt_digit = (int(curr[j]) + direction) % 10
                        nxt = curr[:j] + str(nxt_digit) + curr[(j+1):]
                        if nxt in visited or nxt in deadends:
                            continue
                        else:
                            visited.add(nxt)
                            queue.append(nxt)
            step += 1
        return -1

# @lc code=end

