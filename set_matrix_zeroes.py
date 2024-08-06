class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, columns = len(matrix), len(matrix[0])
        def related_cells(coordinates):
            res = []
            for coordinate in coordinates:
                row, column = coordinate
                res += list(map(lambda x: (row, x), range(columns)))
                res += list(map(lambda x: (x, column), range(rows)))
            return res
        zeros = [(row, column) for row in range(rows) for column in range(columns) if matrix[row][column] == 0]
        for row, column in related_cells(zeros):
            matrix[row][column] = 0