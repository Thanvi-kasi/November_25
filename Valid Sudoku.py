class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create three sets for tracking row, column, and subgrid numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]
        
        # Traverse through each cell in the 9x9 board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num == '.':
                    continue  # Skip empty cells
                
                # Calculate subgrid index
                subgrid_index = (i // 3) * 3 + (j // 3)
                
                # Check if the number is already in the respective row, column, or subgrid
                if num in rows[i] or num in cols[j] or num in subgrids[subgrid_index]:
                    return False
                
                # Add the number to the respective row, column, and subgrid sets
                rows[i].add(num)
                cols[j].add(num)
                subgrids[subgrid_index].add(num)
        
        # If no duplicates were found, the board is valid
        return True
