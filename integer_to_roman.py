class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_value = [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1)
        ]
        res = ''
        for symbol, value in symbol_value:
            res += symbol * (num // value)
            num %= value
        return res
