import math
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap = {}
        if len(nums) == 1:
            return nums[0]
        for key, value in enumerate(nums):
            if value not in hashmap:
                hashmap[value] = 1
            else:
                hashmap[value] += 1
                if hashmap[value] > math.floor(len(nums)/2):
                    return value 