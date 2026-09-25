class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        count = 0
        while n // (2**i) != 0:
            i += 1
            print(i)
        
        for j in range(i-1, -1, -1):
            if (n // (2**j)) == 1:
                n -= 2**j
                count += 1
        return count 