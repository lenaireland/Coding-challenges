def maze_path(matrix, path=None):
    """Traverse T/F maze.  Robot can only move right or down.
    If robot can get to finish, return coords of route.
    Otherwise return None"""

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    finish_r = n_rows - 1
    finish_c = n_cols - 1

    r = 0
    c = 0

    if matrix[0][0] == "F":
        return None


    if r == finish_r and c == finish_c:
        return (r,c)

    try:
        if matrix[r+1][c] == "T":
            value = maze_path(matrix[:][1:], path)
            if value:
                path.append((r,c))
    except:
        pass

    try:
        if matrix[r][c+1] == "T":
            value = maze_path(matrix[1:][:], path)
            if value:
                path.append((r,c))
    except:
        pass

    return path


