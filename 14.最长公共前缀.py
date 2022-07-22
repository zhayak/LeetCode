#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def findCommon(self, str1, str2):
        common = ""
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                common += str1[i]
            else:
                return common
        return common

    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for i in range(1, len(strs)):
            common = self.findCommon(common, strs[i])
        return common

# @lc code=end

