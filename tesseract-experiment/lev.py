def lev(a, b):
    (la, lb) = (len(a), len(b))
    mat = [[-1 for _ in range(lb + 1)] for _ in range(la + 1)]
    for x in range(la + 1):
        mat[x][0] = x
    for y in range(lb + 1):
        mat[0][y] = y
    for x in range(1, la + 1):
        for y in range(1, lb + 1):
            if a[x-1] == b[y-1]:
                mat[x][y] = mat[x-1][y-1]
            else:
                mat[x][y] = min(mat[x-1][y] + 1,
                                mat[x][y-1] + 1,
                                mat[x-1][y-1] + 1)
    return mat[la][lb]
