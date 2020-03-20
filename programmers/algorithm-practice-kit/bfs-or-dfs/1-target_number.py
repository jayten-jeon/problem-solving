answer = 0
def search(n, check, numbers, current, target):
    global answer
    if n == len(numbers):
        if current == target:
            answer += 1
        return
    number = numbers[n]
    check[n] = 1
    search(n + 1, check, numbers, current + number, target)
    search(n + 1, check, numbers, current - number, target)
    check[n] = 0
def solution(numbers, target):  
    global answer
    check = [0 for _ in range(len(numbers))]
    search(0, check, numbers, 0, target)
    return answer
