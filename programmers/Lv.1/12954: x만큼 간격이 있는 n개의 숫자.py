# sol

def solution(x, n):
    answer = [x]
    for i in range(2, n+1):
        answer.append(x*i)
    return answer


# sol2
def solution(x, n):
    return [x*i for i in range(1, n+1)]
