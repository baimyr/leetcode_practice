class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        mt = {(str(i), str(j)): i * j for i in range(1, 10) for j in range(1, 10)}
        res = 0
        for step1, digit1 in enumerate(num1[::-1]):
            if digit1 == '0':
                continue
            for step2, digit2 in enumerate(num2[::-1]):
                if digit2 == '0':
                    continue
                res += mt[(digit1, digit2)] * (10 ** step2) * (10 ** step1)
        return str(res)
