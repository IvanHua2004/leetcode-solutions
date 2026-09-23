class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total = nums1 + nums2
        total = sorted(total)
        if len(total) % 2 == 0:
            return (total[len(total)//2-1] + total[len(total)//2])/2
        else:
            return float(total[len(total)//2])