class Solution:
    def solveNQueens(self, n: int):
        def backtrack(row, cols, diagonals, anti_diagonals, board, results):
            # If we've placed queens in all rows, add the board to the results
            if row == n:
                results.append(["".join(row) for row in board])
                return

            for col in range(n):
                # Check if the column or diagonals are under attack
                if col in cols or (row - col) in diagonals or (row + col) in anti_diagonals:
                    continue

                # Place the queen
                board[row][col] = 'Q'
                # Mark the column and diagonals as under attack
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)

                # Recurse to place the next queen
                backtrack(row + 1, cols, diagonals, anti_diagonals, board, results)

                # Backtrack: remove the queen and unmark the positions
                board[row][col] = '.'
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

        # Initialize results and board
        results = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set(), board, results)
        return results
