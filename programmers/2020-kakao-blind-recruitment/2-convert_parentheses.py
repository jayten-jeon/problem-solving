def is_balanced(p):
    return p.count("(") == p.count(")")

def get_u_v(w):
    for n in range(2, len(w) + 1):
        if is_balanced(w[:n]):
            return (w[:n], w[n:])

def is_right(p):
    if not is_balanced(p):
        return False
    flag = 0
    for p_ in p:
        if p_ is "(":
            flag += 1
        elif flag > 0:
            flag -= 1
    return flag == 0

def convert(w):
    if w is "":
        return w
    u, v = get_u_v(w)
    if is_right(u):
        return u+convert(v)
    tmp = "(" + convert(v) + ")"
    tmp += "".join(["(" if u_ == ")" else ")" for u_ in u[1:-1]])
    return tmp
    
def solution(p):
    answer = convert(p)
    return answer
