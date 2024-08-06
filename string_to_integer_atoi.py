class Solution:
    def myAtoi(self, s: str) -> int:
        res = ''
        for i in s:
            if i.isdigit() or ((i == '-' or i == '+') and res == ''):
                res += i
            elif i == ' ':
                if res:
                    break
                else:
                    continue
            else:
                break
        try:
            res = int(res)
            if res > 2 ** 31 - 1:
                return 2 ** 31 - 1
            if res < -(2 ** 31):
                return -(2 ** 31)
            return res
        except:
            return 0
