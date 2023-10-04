# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

# 제한조건
# num은 int 범위의 정수입니다.
# 0은 짝수입니다.

# sol
def solution(num):
    if num % 2 == 1:
        return "Odd"
    return "Even"
