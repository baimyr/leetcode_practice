class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        nums_len = len(nums)
        left, right = 0, nums_len - 1
        while True:
            pointer = ceil((left + right) / 2)
            if left > right:
                break
            if nums[pointer] > target:
                right = pointer - 1
            elif nums[pointer] < target:
                left = pointer + 1
            else:
                if pointer == 0 or nums[pointer - 1] < target:
                    first = pointer
                    break
                else:
                    right = pointer - 1
        left, right = 0, nums_len - 1
        while True:
            pointer = ceil((left + right) / 2)
            if left > right:
                break
            if nums[pointer] > target:
                right = pointer - 1
            elif nums[pointer] < target:
                left = pointer + 1
            else:
                if pointer == nums_len - 1 or nums[pointer + 1] > target:
                    last = pointer
                    break
                else:
                    left = pointer + 1
        return [first, last]
