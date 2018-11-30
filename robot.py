def maze_path(matrix, r=None, c=None):
    """Traverse T/F maze.  Robot can only move right or down.
    If robot can get to finish, return coords of route.
    Otherwise return None"""

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    if r is None and c is None:
        r = n_rows - 1
        c = n_cols -1
        return maze_path(matrix, r, c)

    # print("Current point is ({},{})".format(r,c))

    if r < 0 or c < 0 or matrix[r][c] is False:
        return False

    if r == 0 and c == 0:
        return [(r,c)]

    up_path = maze_path(matrix, r-1, c)
    left_path = maze_path(matrix, r, c-1)

    if up_path:
        return up_path + [(r,c)]
    elif left_path:
        return left_path + [(r,c)]

    return None


invalid = ([[True, False, False, True, False, True],
           [True, True, False, True, True, True],
           [True, False, False, True, True, True],
           [True, False, True, True, True, True],
           [True, False, True, True, True, True]])

valid =  ([[True, False, False, True, True, True],
           [True, True, True, False, True, True],
           [True, False, True, False, True, True],
           [True, False, True, True, False, True],
           [False, False, False, True, True, True]])

print(maze_path(invalid))

print(maze_path(valid))

