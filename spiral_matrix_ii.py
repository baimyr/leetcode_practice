class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        rows, columns, steps = n - 1, n - 1, n ** 2
        def get_spiral_ids(pos, circle, step):
            poses, x, y = [pos], pos[0], pos[1]
            if steps == step:
                return poses
            if y == circle and x != columns - circle:
                next_pos = (x + 1, y)
            elif x == columns - circle and y != rows - circle:
                next_pos = (x, y + 1)
            elif y == rows - circle and x != circle:
                next_pos = (x - 1, y)
            elif x == circle and y != circle + 1:
                next_pos = (x, y - 1)
            else:
                circle += 1
                next_pos = (x + 1, y)
            return poses + get_spiral_ids(next_pos, circle, step + 1)
        for index, pos in enumerate(get_spiral_ids((0, 0), 0, 1)):
            res[pos[1]][pos[0]] = index + 1
        return  res
