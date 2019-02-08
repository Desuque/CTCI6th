ZERO = 0  # Do not use magic numbers
MINUS_ONE = -1


def main():
    set_zero_rows_cols()


def change_row_col(mat, i, j):
    for x in range(len(mat)):
        if mat[i][x] != ZERO:
            mat[i][x] = MINUS_ONE

    for y in range(len(mat)):
        if mat[y][j] != ZERO:
            mat[y][j] = MINUS_ONE


def set_zero_rows_cols():
    mat = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]

    # Brute force only?
    # First pass

    for x in range(len(mat)):  # Search: how to iterate non NxN matrix in Python 3
        for y in range(len(mat)):
            if mat[x][y] == ZERO:
                change_row_col(mat, x, y)

    for x in range(len(mat)):
        for y in range(len(mat)):
            if mat[x][y] == MINUS_ONE:
                mat[x][y] = ZERO

    print(mat)


if __name__ == '__main__':
    main()