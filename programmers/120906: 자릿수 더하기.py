# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

# sol
def solution(n):
    nums = list(str(n))
    return sum(map(int, nums))


# sol2
def solution(n):
    return sum(int(i) for i in str(n))
