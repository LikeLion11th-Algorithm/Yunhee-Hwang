# sol1
def solution(n):

    x = 1
    print(n % x)

    for i in range(n):
        if n % x == 1:
            return x
        else:
            x += 1
