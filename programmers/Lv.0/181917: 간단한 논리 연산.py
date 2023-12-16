# sol

def solution(x1, x2, x3, x4):

    answer1 = x1 or x2
    answer2 = x3 or x4

    answer = answer1 and answer2
    return answer


# sol2
def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)


# sol3
def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)
