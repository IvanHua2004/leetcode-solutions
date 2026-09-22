class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = [x for x in range(1, n+1)]
        for i in range(0, n):
            if sum(arr[0:i+1]) == sum(arr[i:len(arr)]):
                return i+1
        return -1