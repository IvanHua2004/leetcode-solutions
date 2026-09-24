class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        arr1 = [1]
        arr2 = [1,1]

        if rowIndex == 0:
            return arr1
        elif rowIndex == 1:
            return arr2

        for i in range(rowIndex-1):
            arr1[:] = arr2
            arr2 = [1] * (i+3)
            for j in range(1, len(arr2)-1):
                arr2[j] = arr1[j-1] + arr1[j]

        return arr2
