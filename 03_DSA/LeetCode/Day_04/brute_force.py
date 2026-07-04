class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len = len(nums)
        for i in nums:
            for j in range(len):
                if i == nums[j] :
                    return True
        return False
            