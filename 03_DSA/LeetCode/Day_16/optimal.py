class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        answer = 0
        previous = 0

        for ch in reversed(s):
            value = roman[ch]
            if value < previous:
                answer -= value
            else:
                answer += value
            previous = value
        return answer