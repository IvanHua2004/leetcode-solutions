class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        dupplicates = set()
        result = []
        for i in nums:
            if i not in dupplicates:
                dupplicates.add(i)
                result.append(i)
        
        nums[:] = result
        