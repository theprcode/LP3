# Aim: To write a Python program to design an N-Queens matrix
# with the first Queen placed and use backtracking to place
# the remaining Queens to generate the final N-Queens matrix.

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False

        if col + (row - i) < n and board[i][col + (row - i)] == 1:
            return False

    return True

def solve(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve(board, row + 1, n):
                return True

            board[row][col] = 0

    return False

n = int(input("Enter N: "))

if n < 1:
    print("Please enter a positive number.")
else:
    board = [[0] * n for _ in range(n)]

    # Place the first Queen at position (0, 0).
    board[0][0] = 1

    if solve(board, 1, n):
        print("N-Queens Matrix:")
        for row in board:
            print(row)
    else:
        print("Solution does not exist with the first Queen at (0, 0).")

# Time Complexity: O(N!)
# Space Complexity: O(N^2) for the board and O(N) recursion stack
