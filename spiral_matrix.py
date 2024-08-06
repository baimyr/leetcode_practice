class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, columns, steps = len(matrix) - 1, len(matrix[0]) - 1, len(matrix) * len(matrix[0])

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
        return list(map(lambda pos: matrix[pos[1]][pos[0]], get_spiral_ids((0, 0), 0, 1)))
