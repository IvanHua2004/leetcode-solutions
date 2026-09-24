class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)-1               
        n = len(matrix[0])-1           
        total = (m+1)*(n+1)               
        top = 0                           
        left = 0                         
        leftRight = 0
        upDown = 0
        res = []
        i = 0
        j = 0
        right = True
        down = False                    
        while len(res) < total:         
            # going left or right
            if leftRight == upDown:
                if (i == n and right == True or i == left and right == False):  
                    res.append(matrix[j][i])      
                    if right == True:             
                        top += 1
                    else:
                        m -= 1
                    leftRight += 1
                    down = not down
                    if down == True:
                        j += 1
                    else:
                        j -= 1
                elif right == True:
                    res.append(matrix[j][i])
                    i += 1
                else:
                    res.append(matrix[j][i])
                    i -= 1
            # going up or down
            else:
                if (j == m and down == True) or (j == top and down == False):     
                    res.append(matrix[j][i])       
                    if down == True:            
                        n -= 1
                    else:
                        left += 1
                    upDown += 1
                    right = not right
                    if right == True:
                        i += 1
                    else:
                        i -= 1
                elif down == True:
                    res.append(matrix[j][i])
                    j += 1
                else:
                    res.append(matrix[j][i])
                    j -= 1
        return res