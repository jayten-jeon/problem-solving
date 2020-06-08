class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(target=word, current="", y=0, x=0, visited=[]):
            current = current + board[y][x]
            if len(target) == len(current):
                if target == current:
                    return True
                return False

            visited.append((y, x))
            for i in range(len(current)):
                if target[i] != current[i]:
                    return False
            if y > 0:
                point = (y-1, x)
                if point not in visited:
                    if search(target, current, point[0], point[1], visited +[point]):
                        return True
            if y < len(board)-1:
                point = (y+1, x)
                if point not in visited:
                    if search(target, current, point[0], point[1], visited +[point]):
                        return True
            if x > 0:
                point = (y, x-1)
                if point not in visited:
                    if search(target, current, point[0], point[1], visited +[point]):
                        return True
            if x < len(board[0])-1:
                point = (y, x+1)
                if point not in visited:
                    if search(target, current, point[0], point[1], visited +[point]):
                        return True
        for y in range(len(board)):
            for x in range(len(board[0])):
                if search(y=y, x=x, visited=[]):
                    return True
        return False
