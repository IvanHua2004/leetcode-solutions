class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        reverse = True
        for i in range(0, len(s), k):
            part = s[i:i+k]
            result += part[::-1] if reverse == True else part
            reverse = not reverse
        return result

