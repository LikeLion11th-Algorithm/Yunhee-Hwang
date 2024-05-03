# sol1
def solution(n):

    x = n//2
    return x*(x+1)

# sol2


def solution(n):

    return sum(x for x in range(2, n+1, 2))
