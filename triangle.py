class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ps = []
        for ri, row in enumerate(triangle):
            ps.append([])
            for ci, val in enumerate(row):
                n_1_i = (ri - 1, ci)
                n_2_i = (ri - 1, ci - 1)
                n_1 = None
                n_2 = None
                if n_1_i[0] < 0 or n_1_i[1] < 0 or n_1_i[0] >= len(ps) or ri == ci:
                    n_1 = None
                else:
                    n_1 = ps[n_1_i[0]][n_1_i[1]]
                if n_2_i[0] < 0 or n_2_i[1] < 0 or n_2_i[0] >= len(ps):
                    n_2 = None
                else:
                    n_2 = ps[n_2_i[0]][n_2_i[1]]
                if n_1 is None and n_2 is not None:
                    n = n_2
                if n_2 is None and n_1 is not None:
                    n = n_1
                if n_1 is None and n_2 is None:
                    n = 0
                if n_1 is not None and n_2 is not None:
                    n = min(n_1, n_2)
                p = n + val
                ps[ri].append(p)
        return min(ps[-1])
