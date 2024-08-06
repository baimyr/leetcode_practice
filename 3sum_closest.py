class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        nums_len = len(nums)
        for index1, num1 in enumerate(nums):
            target1 = target - num1
            nums1 = nums[:index1] + nums[index1 + 1:]
            left, right = 0, nums_len - 2
            for index2 in range(nums_len - 1):
                if left >= right:
                    break
                if abs(target - num1 - nums1[left] - nums1[right]) < abs(target - res):
                    res = num1 + nums1[left] + nums1[right]
                if nums1[left] + nums1[right] > target1:
                    right -= 1
                elif nums1[left] + nums1[right] < target1:
                    left += 1
                else:
                    return num1 + nums1[left] + nums1[right]
        return res
