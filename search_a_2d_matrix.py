class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0, len(matrix) - 1
        while l <= h:
            pointer = ceil((h + l) / 2)
            if matrix[pointer][-1] < target:
                l = pointer + 1
            elif matrix[pointer][0] > target:
                h = pointer - 1
            else:
                l1, h1 = 0, len(matrix[pointer]) - 1
                while l1 <= h1:
                    pointer1 = ceil((h1 + l1) / 2)
                    if matrix[pointer][pointer1] < target:
                        l1 = pointer1 + 1
                    elif matrix[pointer][pointer1] > target:
                        h1 = pointer1 - 1
                    else:
                        return True
                return False
        return False
