class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        reverse = ""
        for i in range(len(cleaned) - 1, -1, -1):
            reverse += cleaned[i]
        return cleaned == reverse