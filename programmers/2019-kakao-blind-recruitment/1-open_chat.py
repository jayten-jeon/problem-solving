def solution(record):
    answer = []
    # users = dict()
    # for r in record:
    #     splitted_r = r.split(" ")
    #     if splitted_r[0] != "Leave":
    #         users[splitted_r[1]] = splitted_r[2]
    enter = "{}님이 들어왔습니다."
    leave = "{}님이 나갔습니다."
    record = [r.split(" ") for r in record]
    users = {r[1]:r[2] for r in record if r[0] != 'Leave'}
    answer = [enter.format(users[r[1]]) if r[0] == 'Enter' else leave.format(users[r[1]]) for r in record if r[0] != 'Change']
    return answer
