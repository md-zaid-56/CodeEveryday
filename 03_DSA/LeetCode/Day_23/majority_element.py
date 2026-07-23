
class Solution:
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num in count:
            if count[num] > len(nums) // 2:
                return num
