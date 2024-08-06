class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        multiplier = 1
        sm = 0
        for i in range(n):
            if s[i] == '(':
                multiplier *= 2
            else:
                multiplier /= 2
                if s[i - 1] == '(':
                    sm += multiplier
        return int(sm)