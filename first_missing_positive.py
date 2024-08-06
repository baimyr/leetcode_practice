class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] > n:
                nums[i] = 0
        for i in range(n):
            if nums[i] != 0:
                if -abs(nums[abs(nums[i]) - 1]) != 0:
                    nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
                else:
                    nums[abs(nums[i]) - 1] = -n
            else:
                nums[i] = n
        for i in range(1, n + 1):
            if nums[i - 1] >= 0:
                return i
        return n + 1
