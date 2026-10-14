from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]):
        for row in range(9):
            seen = set()
            for col in range(9):
                value = board[row][col]
                if value.isdigit():
                    if value in seen:
                        return False
                    seen.add(value)
        for col in range(9):
            seen = set()
            for row in range(9):
                value = board[row][col]
                if value.isdigit():
                    if value in seen:
                        return False
                    seen.add(value)                
        for max_rows in range(0, 9, 3):
            for max_cols in range(0, 9, 3):
                seen = set()
                for row in range(max_rows, max_rows + 3):
                    for col in range(max_cols, max_cols + 3):
                        value = board[row][col]
                        if value.isdigit():
                            if value in seen:
                                return False
                            seen.add(value)
        return True                        
                                 