# sol1
def solution(array, n):
    num = 0
    for string in array:
        if string == n:
            num += 1
    return num


# sol2
def solution(array, n):
    return array.count(n)
