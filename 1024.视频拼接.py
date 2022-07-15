#
# @lc app=leetcode.cn id=1024 lang=python3
#
# [1024] 视频拼接
#

# @lc code=start
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips = sorted(clips, key=lambda x: (x[0], -x[1]))
        cnt = 0
        i = 0
        curr_end, next_end = 0, 0
        while i < len(clips) and clips[i][0] <= curr_end:
            while i < len(clips) and clips[i][0] <= curr_end:
                next_end = max(next_end, clips[i][1])
                i += 1
            curr_end = next_end
            cnt += 1
            if curr_end >= time:
                return cnt
        return -1

# @lc code=end

