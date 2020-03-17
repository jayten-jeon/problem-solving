def is_right(n, rows, cols):
    for y in range(n + 1):
        for x in range(n + 1):
            if cols[y][x] == 1:
                if not (y == 0 or rows[y][x] == 1 or rows[y][x - 1] or cols[y - 1][x] == 1):
                    return False
            if rows[y][x] == 1:
                if not (cols[y - 1][x] == 1 or cols[y - 1][x + 1] == 1 or (rows[y][x - 1] == 1 and rows[y][x + 1] == 1)):
                    return False
    return True
            
def solution(n, build_frame):
    answer = []
    rows = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    cols = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    board = [cols, rows]
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:
            board[a][y][x] = 0
            if not is_right(n, rows, cols):
                board[a][y][x] = 1
        else:
            board[a][y][x] = 1
            if not is_right(n, rows, cols):
                board[a][y][x] = 0
    for x in range(n + 1):
        for y in range(n + 1):
            for a in range(2):
                if board[a][y][x] == 1:
                    answer.append([x, y, a])
    return answer
