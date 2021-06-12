# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

from collections import defaultdict
def solveSudoku(A):
    def dfs(A, rows, cols, blocks, q):
        if not q:
            return True
        
        i, j = q[0]
        k = (i//3, j//3)
        
        for num in range(1, 10):
            num = str(num)
            if num not in rows[i] and num not in cols[j] and num not in blocks[k]:
                A[i][j] = num
                rows[i].add(num)
                cols[j].add(num)
                blocks[k].add(num)
                
                if dfs(A, rows, cols, blocks, q[1:]):
                    return True
                
                A[i][j] = "."
                rows[i].remove(num)
                cols[j].remove(num)
                blocks[k].remove(num)
        
        return False
                
    
    q = []
    rows, cols, blocks = defaultdict(set), defaultdict(set), defaultdict(set)
    
    for i in range(9):
		for j in range(9):
		    if A[i][j] == ".":
		        q.append((i, j))
		    else:
		        rows[i].add(A[i][j])
		        cols[j].add(A[i][j])
		        blocks[(i//3, j//3)].add(A[i][j])
    
    dfs(A, rows, cols, blocks, q)
        
                    
