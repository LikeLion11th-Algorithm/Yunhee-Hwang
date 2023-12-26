# sol

def solution(dot):
    answer = 0
    if dot[0] < 0:
        answer += 2
        if dot[1] < 0:
            answer += 1
    else:
        answer += 1
        if dot[1] < 0:
            answer *= 4
    return answer


# sol2
def solution(dot):
    quad = [(3, 2), (4, 1)]
    return quad[dot[0] > 0][dot[1] > 0]
