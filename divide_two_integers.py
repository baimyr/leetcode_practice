class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend == 0 or divisor == 0:
            return 0
        pointer, carry, res, digits = 0, 0, 0, ceil(log(dividend, 10)) + 1
        while pointer < digits:
            res = res * 10
            rank_multiplier = 10 ** (digits - pointer - 1)
            pointer_digit = (dividend // rank_multiplier) % 10
            current_dividend = carry * 10 + pointer_digit
            if current_dividend < divisor:
                carry = current_dividend
                pointer += 1
                continue
            carry = 0
            remainder = current_dividend
            answer = 0
            while remainder >= divisor:
                answer += 1
                remainder -= divisor
            res += answer
            carry = remainder
            pointer += 1
        final_res = -res if negative else res
        if final_res > 2147483647:
            return 2147483647
        elif final_res < -2147483648:
            return -2147483648
        else:
            return final_res
