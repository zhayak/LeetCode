# Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1, p2 = 0, 0
        l1, l2 = len(nums1), len(nums2)
        last = current = 0
        for i in range((l1 + l2) // 2 + 1):
            last = current
            if p1 < l1 and p2 < l2:
                if nums1[p1] < nums2[p2]:
                    current = nums1[p1]
                    p1 += 1
                else:
                    current = nums2[p2]
                    p2 += 1
            elif p1 < l1:
                current = nums1[p1]
                p1 += 1
            else:
                current = nums2[p2]
                p2 += 1

        if (l1 + l2) % 2 == 0:
            return (last + current) / 2
        else:
            return current

# Use two pointers
