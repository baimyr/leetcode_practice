class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split('/')
        d = deque()
        for s in l:
            if s == '' or s == '.':
                continue
            if s == '..':
                if d:
                    d.pop()
                continue
            d.append(s)
        return '/' + '/'.join(d)
