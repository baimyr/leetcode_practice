class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        colums = defaultdict(list)
        boxes = defaultdict(list)
        def func1(tup):
            row, row_numbers = tup[0], tup[1]
            box_row = row // 3
            def func2(tup):
                index, number = tup[0],  tup[1]
                if not number.isdigit():
                    return False
                box_column = index // 3
                if number in rows[row]:
                    return True
                else:
                    rows[row].append(number)
                if number in colums[index]:
                    return True
                else:
                    colums[index].append(number)
                if number in boxes[(box_column, box_row)]:
                    return True
                else:
                    boxes[(box_column, box_row)].append(number)
            return any(map(func2, enumerate(row_numbers)))
        return not any(map(func1, enumerate(board)))
