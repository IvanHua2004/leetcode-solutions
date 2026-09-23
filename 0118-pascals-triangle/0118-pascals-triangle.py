class Solution(object):
    def generate(self, numRows):
        result = []

        for r in range(numRows):
            row = [1] * (r+1)

            for j in range(1, r):
                above = result[r-1]
                row[j] = above[j-1] + above[j]
            result.append(row) 
        return result

