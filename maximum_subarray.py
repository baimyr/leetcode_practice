class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c, max_c = nums[0], nums[0]
        for num in nums[1:]:
            c = max(c + num, num)
            max_c = max(c, max_c)
        return max_c