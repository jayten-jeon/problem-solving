def solution(brown, red):
    wide = brown + red
    pairs = [(i, int(wide / i))for i in range(1, wide + 1) if wide % i == 0 and i >= int(wide / i)]
    for x, y in pairs:
        if brown == 2*x + 2*(y-2) and red == (y-2) * (x - 2):
            return [x, y]
