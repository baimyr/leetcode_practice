class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        for index, num in enumerate(nums):
            if index > max_pos:
                break
            max_pos = max(max_pos, index + num)
        return max_pos >= len(nums) - 1