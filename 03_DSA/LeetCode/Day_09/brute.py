class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for char in s:
            while index < len(t) and t[index] != char:
                index += 1
            if index == len(t):
                return False
            index += 1
        return True