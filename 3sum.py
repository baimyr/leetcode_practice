class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        child_nums_len = len(nums) - 1
        for main_index, main_num in enumerate(nums):
            target = -main_num
            child_nums = nums[:main_index] + nums[main_index + 1:]
            start = 0
            finish = child_nums_len - 1
            for _ in range(child_nums_len):
                if start == finish or start >= child_nums_len or finish <= 0:
                    break
                current_sum = child_nums[start] + child_nums[finish]
                if current_sum > target:
                    finish -= 1
                elif current_sum < target:
                    start += 1
                else:
                    res.add(tuple(sorted([main_num, child_nums[start], child_nums[finish]])))
                    finish -= 1
                    start += 1
        return res
