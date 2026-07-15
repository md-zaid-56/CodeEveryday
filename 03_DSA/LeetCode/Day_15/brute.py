from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            total = 0
            for j in range(i + 1):
                total += nums[j]
            ans.append(total)
        return ans