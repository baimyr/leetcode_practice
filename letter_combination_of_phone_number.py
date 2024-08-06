class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letters = [None, ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'],
                         ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
                         ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        def combinations(initial, nums):
            ans = []
            if len(nums) == 0:
                return []
            letters = digit_letters[int(nums[0]) - 1]
            if len(nums) == 1:
                for letter in letters:
                    ans.append(initial + letter)
            else:
                for letter in letters:
                    ans.extend(combinations(initial + letter, nums[1:]))
            return ans

        return combinations('', digits)
