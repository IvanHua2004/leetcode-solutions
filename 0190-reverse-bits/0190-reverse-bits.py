class Solution:
    def reverseBits(self, n: int) -> int:
        i = 0
        total = 0
        while (n // (2**i)) != 0:
            i += 1
        
        result = ""
        for j in range(i-1, -1, -1):
            if n // (2**j) == 1:
                result += "1" 
                n -= (2**j)
            else:
                result += "0" 
        
        for j in range(32-len(result)):
            result = "0" + result

        for k, value in enumerate(result):
            if value == "1":
                total += 2**k
                
        return total

            
