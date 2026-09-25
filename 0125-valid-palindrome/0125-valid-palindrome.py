class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""
        for i in s:
            if i.isalnum():
                palindrome += i.lower()
        


        left = 0
        right = len(palindrome)-1
        while left < right:
            if palindrome[left] != palindrome[right]:
                return False
            left += 1
            right -= 1
        return True
