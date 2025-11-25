class Solution:
    def totalNQueens(self, n: int) -> int:
        # Helper function to perform backtracking
        def backtrack(row, columns, diag1, diag2):
            if row == n:
                return 1  # Found a valid arrangement
            
            solutions = 0
            for col in range(n):
                # Check if column or diagonals are under attack
                if col in columns or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Place the queen and move to the next row
                columns.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                solutions += backtrack(row + 1, columns, diag1, diag2)

                # Backtrack: Remove the queen
                columns.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

            return solutions

        # Set to track the columns and diagonals that are already occupied
        columns = set()
        diag1 = set()
        diag2 = set()

        # Start backtracking from row 0
        return backtrack(0, columns, diag1, diag2)
