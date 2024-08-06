class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums)
        while l <= r and l < len(nums):
            if nums[l] == 0:
                del nums[l]
                nums.insert(0, 0)
                if nums[l] == 0:
                    l += 1
            elif nums[l] == 2:
                del nums[l]
                nums.append(2)
                r -= 1
            elif nums[l] == 1:
                l += 1
