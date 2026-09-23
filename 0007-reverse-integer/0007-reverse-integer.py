class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        negative = False
        stack = []
        for i in string:
            if i == "-":
                negative = True
            else:
                stack.append(i)
        result = ""
        if negative == True:
            result += "-"
        
        for i in range(len(stack)):
            result += stack.pop()

        result = int(result)
        if (result > 2**31-1) or (result < -2**31):
            return 0
        return result
                
            