class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        digits = floor(log(x, 10)) + 1
        for step in range(1, ceil(digits / 2) + 1):
            if x // (10 ** (digits - step)) % 10 != x % (10 ** step) // (10 ** (step - 1)):
                return False
        return True
