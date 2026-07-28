# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, name="Matrix"):
    """Reads a matrix of size rows x cols from user input row by row."""
    print(f"\nEntering {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1}: ").split()
        row = [int(val) for val in row_input]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """Prints a matrix in a neat grid format."""
    for row in matrix:
        print(" ".join(f"{val:>3}" for val in row))


# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
def transpose_matrix(matrix):
    """Computes and returns the transpose of an M x N matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize an N x M matrix filled with 0s
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
def add_matrices(matrix_a, matrix_b):
    """Computes and returns the element-wise sum of two M x N matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
def multiply_matrices(matrix_a, matrix_b):
    """Computes and returns the product of matrix A (M x N) and B (N x P)."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    # Resulting matrix size is M x P
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


def main():
    print("=== PART A: TRANSPOSE A MATRIX ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    matrix_a = read_matrix(m, n, "Matrix A")

    print("\nOriginal Matrix:")
    print_matrix(matrix_a)

    print("\nTransposed Matrix:")
    transposed = transpose_matrix(matrix_a)
    print_matrix(transposed)

    print("\n" + "=" * 40)
    print("=== PART B: ADD TWO MATRICES ===")
    print(f"Reading Matrix B of same dimension ({m}x{n}):")
    matrix_b = read_matrix(m, n, "Matrix B")

    print("\nMatrix A + Matrix B:")
    added = add_matrices(matrix_a, matrix_b)
    print_matrix(added)

    print("\n" + "=" * 40)
    print("=== PART C: MULTIPLY TWO MATRICES ===")
    p = int(input(f"Enter number of columns for Matrix C to multiply with A ({n} x P): "))
    matrix_c = read_matrix(n, p, "Matrix C")

    print("\nMatrix A * Matrix C:")
    product = multiply_matrices(matrix_a, matrix_c)
    print_matrix(product)


if __name__ == "__main__":
    main()
