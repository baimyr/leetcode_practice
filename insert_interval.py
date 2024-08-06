class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = deque()
        m = newInterval.copy()
        for interval in intervals:
            if interval[0] >= m[0] and m[1] >= interval[1]:
                continue
            if interval[1] >= m[0] and interval[0] < m[0]:
                m[0] = min(interval[0], m[0])
            if interval[0] <= m[1] and interval[1] > m[1]:
                m[1] = max(interval[1], m[1])
            if interval[1] < m[0] or interval[0] > m[1]:
                if res:
                    if res[-1][1] < m[0] and interval[0] > m[1]:
                        res.append(m)
                else:
                    if interval[0] > m[1]:
                        res.append(m)
                res.append(interval)
        if not res or res[-1][1] < m[0]:
            res.append(m)
        return res
