class Solution:
    def solveSudoku(self, board):
        def is_valid(r, c, ch):
            block = (r // 3) * 3 + (c // 3)
            return (ch not in rows[r] 
                    and ch not in cols[c] 
                    and ch not in boxes[block])

        def place_number(r, c, ch):
            board[r][c] = ch
            rows[r].add(ch)
            cols[c].add(ch)
            boxes[(r // 3) * 3 + (c // 3)].add(ch)

        def remove_number(r, c, ch):
            board[r][c] = '.'
            rows[r].remove(ch)
            cols[c].remove(ch)
            boxes[(r // 3) * 3 + (c // 3)].remove(ch)

        def backtrack(pos=0):
            if pos == 81:
                return True

            r, c = divmod(pos, 9)
            if board[r][c] != '.':
                return backtrack(pos + 1)

            for ch in "123456789":
                if is_valid(r, c, ch):
                    place_number(r, c, ch)
                    if backtrack(pos + 1):
                        return True
                    remove_number(r, c, ch)

            return False

        # Track used values
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Initialize sets with existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        backtrack()
