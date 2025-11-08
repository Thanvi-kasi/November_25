class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        # Helper function to check if a number can be placed in the given position
        def is_valid(row, col, num):
            # Check if the number is already used in the row, column, or 3x3 sub-grid
            return not (num in rows[row] or num in cols[col] or num in boxes[box_index(row, col)])

        # Helper function to calculate the box index
        def box_index(row, col):
            return (row // 3) * 3 + (col // 3)

        # Set of numbers already used in each row, column, and 3x3 sub-grid
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Initialize sets with the current numbers in the board
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index(r, c)].add(num)

        # Backtracking function to solve the Sudoku
        def backtrack():
            # Find the next empty cell (represented by '.')
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in '123456789':
                            if is_valid(r, c, num):
                                # Place the number and update sets
                                board[r][c] = num
                                rows[r].add(num)
                                cols[c].add(num)
                                boxes[box_index(r, c)].add(num)

                                # Recurse to solve the next cell
                                if backtrack():
                                    return True

                                # Backtrack: remove the number and reset sets
                                board[r][c] = '.'
                                rows[r].remove(num)
                                cols[c].remove(num)
                                boxes[box_index(r, c)].remove(num)

                        # If no valid number is found, return False to backtrack
                        return False
            return True  # All cells filled successfully

        # Start the backtracking process
        backtrack()
