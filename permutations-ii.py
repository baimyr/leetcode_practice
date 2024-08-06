class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        res = []
        for index, num in enumerate(nums):
            if num in nums[:index]:
                continue
            for res1 in self.permuteUnique(nums[:index] + nums[index + 1:]):
                res.append([num] + res1)
        return res
