class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        l = len(s)
        res = []
        for i1 in range(0, l):
            int1 = int(s[:i1 + 1])
            if str(int1) != s[:i1 + 1]:
                continue
            if not (0 <= int1 <= 255):
                continue
            for i2 in range(i1 + 1, l):
                int2 = int(s[i1 + 1:i2 + 1])
                if str(int2) != s[i1 + 1:i2 + 1]:
                    continue
                if not (0 <= int2 <= 255):
                    continue
                for i3 in range(i2 + 1, l):
                    int3 = int(s[i2 + 1:i3 + 1])
                    if str(int3) != s[i2 + 1:i3 + 1]:
                        continue
                    if not (0 <= int3 <= 255):
                        continue
                    if i3 + 1 >= l:
                        continue
                    int4 = int(s[i3 + 1:])
                    if str(int4) != s[i3 + 1:]:
                        continue
                    if not (0 <= int4 <= 255):
                        continue
                    res.append('{}.{}.{}.{}'.format(int1, int2, int3, int4))
        return res