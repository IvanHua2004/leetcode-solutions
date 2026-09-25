class Solution:
    def addDigits(self, num: int) -> int:
        res = str(num)
        while len(res) != 1:
            total = 0
            for i in res:
                total += int(i)
            res = str(total)
        return int(res)

