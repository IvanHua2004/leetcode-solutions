class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        for key, value in hashmap.items():
            if value == 1:
                return key