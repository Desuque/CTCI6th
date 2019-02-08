def main():
    rotate_matrix_90_degrees()


def rotate_matrix_90_degrees():
    mat = [[1, 2], [3, 4]]

    n = len(mat)

    for x in range(len(mat)//2):
        for y in range(len(mat)):
            aux = mat[x][y]
            mat[x][y] = mat[y][n - 1 - x]
            mat[y][n - 1 - x] = mat[n - 1 - y][n - 1 - x]
            mat[n - 1 - y][n - 1 - x] = mat[n - 1 - y][x]
            mat[n - 1 - y][x] = aux

    print(mat)


if __name__ == '__main__':
    main()