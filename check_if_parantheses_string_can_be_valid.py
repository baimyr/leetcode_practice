class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0 or (s[0] == ')' and locked[0] == '1') or (s[-1] == '(' and locked[-1] == '1'):
            return False
        opened, closed, qty, brackets = 0, 0, len(s), len(s) / 2
        undefined = 0
        for ptr in range(qty):
            c = s[ptr]
            l = locked[ptr] == '1'
            if l:
                if c == '(':
                    opened += 1
                else:
                    closed += 1
                    if closed > opened and undefined > 0:
                        opened += 1
                        undefined -= 1
            else:
                undefined += 1
            if closed > opened:
                return False
        opened, closed, undefined = 0, 0, 0
        for ptr in reversed(range(qty)):
            c = s[ptr]
            l = locked[ptr] == '1'
            if l:
                if c == '(':
                    opened += 1
                    if opened > closed and undefined > 0:
                        closed += 1
                        undefined -= 1
                else:
                    closed += 1
            else:
                undefined += 1
            if opened > closed:
                return False
        return True
