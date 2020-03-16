def rotate(key):
    tmp = key.copy()
    n = len(key)
    key = [[tmp[y][x] for y in range(n-1, -1, -1)] for x in range(n)]
    return key

def extend_lock(lock, key_size, lock_size):
    lock = [[0 for _ in range(2*(key_size-1) + lock_size)] for _ in range(key_size - 1)] + [[0 for _ in range(key_size - 1)] + row + [0 for _ in range(key_size - 1)] for row in lock] + [[0 for _ in range(2*(key_size-1) + lock_size)] for _ in range(key_size - 1)]
    return lock
    
def is_possible(key, lock, x, y, key_size, lock_size):
    tmp = [row.copy() for row in lock]
    for i in range(key_size):
        for j in range(key_size):
            tmp[y + i][x + j] += key[i][j]
    tmp = [row[key_size-1: key_size + lock_size - 1] for row in tmp[key_size-1: key_size + lock_size - 1]]
    if sum(tmp, []).count(1) == pow(lock_size, 2):
        return True
    return False
def solution(key, lock):
    key_size = len(key)
    lock_size = len(lock)
    lock = extend_lock(lock, key_size, lock_size)
    for y in range(key_size + lock_size - 1):
        for x in range(key_size + lock_size - 1):
            for _ in range(4):
                if is_possible(key, lock, x, y, key_size, lock_size):
                    return(True)
                key = rotate(key)
    return (False)
