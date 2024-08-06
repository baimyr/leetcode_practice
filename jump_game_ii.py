class Solution:
    def jump(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 1:
            return 0
        stop, next_stop, steps = nums[0], nums[0], 0
        for index, num in enumerate(nums):
            next_stop = max(next_stop, index + num)
            if index == stop or (index == nums_len - 1 and stop > index):
                stop, steps = next_stop, steps + 1
        return steps
