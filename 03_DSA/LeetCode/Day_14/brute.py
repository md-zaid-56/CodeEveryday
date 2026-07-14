class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = str(x)
        reverse = original[::-1]
        return original == reverse