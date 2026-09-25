class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        left, right = 0, 20         
        while left <= right:
            mid = (left + right) // 2
            val = 3 ** mid
            if val == n:
                return True
            elif val < n:
                left = mid + 1
            else:
                right = mid - 1
        return False