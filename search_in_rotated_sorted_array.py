class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while True:
            pointer = floor((left + right) / 2)
            print(left, right)
            if nums[pointer] == target:
                return pointer
            if left >= right:
                print('broke')
                break
            if nums[right] < nums[left]:
                if nums[pointer] > nums[right]:
                    if target < nums[pointer] and target > nums[right]:
                        right = pointer - 1
                    else:
                        left = pointer + 1
                else:
                    if target > nums[pointer] and target <= nums[right]:
                        left = pointer + 1
                    else:
                        right = pointer - 1
            else:
                if nums[pointer] > target:
                    right = pointer - 1
                else:
                    left = pointer + 1
        return -1
