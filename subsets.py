class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums_len = len(nums)
        for i in range(nums_len):
            s = []
            s.append([nums[i]])
            for i1 in range(i + 1, nums_len):
                for i2 in range(len(s)):
                    s.append(s[i2] + [nums[i1]])
            ans.extend(s)
        return ans
