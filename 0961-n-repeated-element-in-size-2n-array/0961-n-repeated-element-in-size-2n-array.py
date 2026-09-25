class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
                if hashmap[i] == len(nums)//2:
                    return i