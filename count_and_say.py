class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(n - 1):
            res = self.say(res)
        print(res)
        return res

    def say(self, ds):
        ans = ''
        p, c = None, 0
        for i, s in enumerate(ds):
            if s != p and i != 0:
                ans += str(c) + str(p)
                c = 1
            if s == p or i == 0:
                c += 1
            p = s
        ans += str(c) + str(p)
        return ans
