def check_query(query, words):
    idx = query.index("?")
    n = query.count("?")
    if idx > 0:
        return sum([word[:-n] == query[:-n] for word in words])
    return sum([word[n:] == query[n:] for word in words])
def solution(words, queries):
    answer = [check_query(query, words) for query in queries]
    return answer
