class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(len(nums1)-n, len(nums1)):
            nums1[i] = nums2[i-(len(nums1)-n)]
        nums1[:] = sorted(nums1)