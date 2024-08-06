class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s, nums = k - 1, list(map(str, range(1, n + 1)))
        def f(ans, step):
            nonlocal s
            divisor = factorial(n - step - 1)
            index = s // divisor
            s %= divisor
            return ans + nums.pop(index)
        return reduce(f, range(n), '')