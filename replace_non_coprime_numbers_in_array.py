class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = deque()
        for num in nums:
            lcm_value = num
            if num != 1:
                while stack:
                    num1 = stack.pop()
                    gcd_value = gcd(lcm_value, num1)
                    if gcd_value != 1:
                        lcm_value = (int(lcm_value / gcd_value)) * (int(num1 / gcd_value)) * gcd_value
                    else:
                        stack.append(num1)
                        break
            stack.append(lcm_value)
        return stack
