def solution(brown, red):
    wide = brown + red
    answer = [(i, int(wide / i)) for i in range(wide, 0, -1) if wide % i == 0 and (brown == 2*i + 2*(int(wide / i) -2) and red == (int(wide / i)-2) * (i - 2)) and i >= int(wide / i)]
    return list(answer[0])
