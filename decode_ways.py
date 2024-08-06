class Solution:
    def numDecodings(self, s: str) -> int:
        two_digits = list(map(str, range(10, 27)))
        ways, last_symbol = 0, ''
        for symbol in s:
            if last_symbol == '':
                if symbol == '0':
                    return 0
                ways += 1
                blocked_end = 0
            else:
                if symbol == '0':
                    if last_symbol + symbol not in two_digits:
                        return 0
                    ways -= blocked_end
                    new_blocked_end = ways
                elif last_symbol + symbol in two_digits:
                    new_blocked_end = ways - blocked_end
                    ways = (ways * 2) - blocked_end
                else:
                    new_blocked_end = 0
                blocked_end = new_blocked_end
            last_symbol = symbol
        return ways
