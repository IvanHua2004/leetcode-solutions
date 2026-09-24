class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        i = None
        left = 0
        right = len(matrix)-1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                i = mid
                break
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        
        if i == None:
            return False

        newLeft = 0
        newRight = len(matrix[i])-1
        while newLeft <= newRight:
            mid = newLeft + (newRight-newLeft) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] < target:
                newLeft = mid + 1
            else:
                newRight = mid - 1
        return False 

