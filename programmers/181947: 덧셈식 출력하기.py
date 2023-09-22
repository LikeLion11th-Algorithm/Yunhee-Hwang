# 두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.
# a + b = c

# sol
a, b = map(int, input().strip().split(' '))

# a=4, b=5일 경우, '4 + 5 = 9'로 출력됨, print문 쓸 때 쉼표 쓰면 자동으로 공백처리 됨
print(f'{a} + {b} =', a + b)
