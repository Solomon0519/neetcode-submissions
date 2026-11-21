class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        from collections import defaultdict

        row_lookup = defaultdict(dict)
        col_lookup = defaultdict(dict)
        square_lookup = defaultdict(dict)

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                
                if element == '.':
                    continue
                else:
                    row_lookup[i][element] = row_lookup[i].get(element, 0) + 1
                    col_lookup[j][element] = col_lookup[j].get(element, 0) + 1
                    square_index = (i // 3) * 3 + (j // 3)
                    square_lookup[square_index][element] = square_lookup[square_index].get(element, 0) + 1 

        for row in row_lookup.values():
            for value in row.values():
                if value > 1:
                    return False

        for col in col_lookup.values():
            for value in col.values():
                if value > 1:
                    return False

        for square in square_lookup.values():
            for value in square.values():
                if value > 1:
                    return False
        return True