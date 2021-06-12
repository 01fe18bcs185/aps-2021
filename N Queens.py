# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Example
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

def solveNQueens(n):
    def create_board(state):
        board = []
        for row in state:
            board.append("".join(row))
        return board

    def backtrack(r, col, diag, anti_diag, state):
        if r == n:
            res.append(create_board(state))
            return
        
        for c in range(n):
            if c not in col and (r+c) not in anti_diag and (r-c) not in diag:
                state[r][c] = "Q"
                backtrack(r+1, col.union({c}), diag.union({r-c}), anti_diag.union({r+c}), state)
                state[r][c] = "."
    
    res = []
    empty_board = [["." for _ in range(n)] for _ in range(n)]
    backtrack(0, set(), set(), set(), empty_board)
    
    return res
