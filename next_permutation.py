class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for pointer in reversed(range(len(nums) - 1)):
            if nums[pointer] < nums[pointer + 1]:
                a = nums[pointer]
                first_slice_number = None
                for index in reversed(range(pointer + 1, len(nums))):
                    p = nums[index]
                    if p > a:
                        nums[index] = a
                        first_slice_number = p
                        break
                nums[pointer] = first_slice_number
                nums[pointer + 1:] = list(reversed(nums[pointer + 1:]))
                return
        nums[::] = nums[::-1]
