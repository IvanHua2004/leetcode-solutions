class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            sumNum = sum([int(char) for char in str(num)])
            if sumNum == i:
                return i
        return -1 