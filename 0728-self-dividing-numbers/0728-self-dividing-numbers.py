class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        arr = [x for x in range(left, right+1)]
        result = []
        for i in arr:
            selfDividing = True
            for p in [int(num) for num in str(i)]:
                if p == 0: 
                    selfDividing = False
                    break
                if i % p != 0:
                    selfDividing = False
            if selfDividing == True:
                result.append(i)
        return result
        