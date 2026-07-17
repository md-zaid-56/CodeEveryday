class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        answer = ""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                answer += chars[0]
            else:
                break
        return answer