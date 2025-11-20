class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        
        # Step 1: Transpose the matrix (convert rows to columns)
        for i in range(n):
            for j in range(i + 1, n):  # Only swap above the diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
