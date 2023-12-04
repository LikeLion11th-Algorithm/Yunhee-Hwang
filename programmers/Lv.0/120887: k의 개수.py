# sol

def solution(i, j, k):

    str_j = str(j)
    k = str(k)
    answer = 0
    str_j = list(map(str, str_j))

    while i < (j+1):
        str_i = list(map(str, str(i)))
        for x in str_i:
            if str(k) == x:
                answer += 1
        i += 1
    return answer


# sol2
def solution(i, j, k):
    answer = sum([str(i).count(str(k)) for i in range(i, j+1)])
    return answer
