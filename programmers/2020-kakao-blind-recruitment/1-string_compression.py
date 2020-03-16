def compress(s, n):
    comp_s = ""
    count = 1
    for i in range(0, len(s) + 1, n):
        if s[i:i+n] == s[i + n: i+ 2*n]:
            count += 1
        elif count == 1:
            comp_s += s[i:i+n]
        else:
            comp_s += str(count)
            comp_s += s[i:i+n]
            count = 1
    return comp_s                                                                                                            
def solution(s):
    answer = 0
    comp = s
    for i in range(1, int(len(s) / 2) + 1):
        tmp = compress(s, i)
        if len(tmp) < len(comp):
            comp = tmp
    answer = len(comp)
return answer
