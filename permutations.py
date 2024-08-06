class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [[nums[0]]]
        for index, num in enumerate(nums):
            permutations = self.permute(nums[:index] + nums[index + 1:])
            for permutation in permutations:
                res.append(permutation + [num])
        return res
