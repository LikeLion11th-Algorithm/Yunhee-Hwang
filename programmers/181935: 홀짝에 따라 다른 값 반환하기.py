# 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

# sol
def solution(n):
    array = []
    num = 0

    for i in range(1, n+1):
        array.append(i)

    if n % 2 == 1:
        for j in range(1, n+1):
            if j % 2 == 1:
                num += j
    if n % 2 == 0:
        for p in range(1, n+1):
            if p % 2 == 0:
                num += p*p
    return num


# sol2

def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)
