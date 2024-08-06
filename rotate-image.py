class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        grid = len(matrix) - 1
        def replace_element(row, column, depth=4):
            new_value = matrix[row][column]
            new_row = column
            new_column = grid - row
            if depth:
                replace_element(new_row, new_column, depth-1)
            matrix[new_row][new_column] = new_value
        for row, elements in enumerate(matrix[:ceil(grid / 2)]):
            for column, element in enumerate(elements[row:grid - row], start=row):
                replace_element(row, column)