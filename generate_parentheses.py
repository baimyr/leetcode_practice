class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def bracket(to_open, to_close, pstr):
            res = []
            if to_open == to_close == 0:
                return [pstr]
            if to_open > 0:
                res.extend(bracket(to_open - 1, to_close, pstr + '('))
            if to_close > 0 and to_close - to_open > 0:
                res.extend(bracket(to_open, to_close - 1, pstr + ')'))
            return res
        return bracket(n, n, '')
