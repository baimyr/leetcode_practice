class Solution:
    def isValid(self, s: str) -> bool:
        po, pc, fo, fc, so, sc = 0, 0, 0, 0, 0, 0
        d = deque()
        n = len(s)
        r = {'{': '}', '[': ']', '(': ')'}
        for i in range(len(s)):
            if s[i] in ('{', '[', '('):
                d.append(s[i])
            else:
                if len(d) == 0:
                    return False
                l = d.pop()
                if r[l] != s[i]:
                    return False
            if s[i] == '(':
                po += 1
            if s[i] == ')':
                pc += 1
            if s[i] == '{':
                fo += 1
            if s[i] == '}':
                fc += 1
            if s[i] == '[':
                so += 1
            if s[i] == ']':
                sc += 1
        if po - pc != 0 or fo - fc != 0 or so - sc != 0:
            return False
        return True