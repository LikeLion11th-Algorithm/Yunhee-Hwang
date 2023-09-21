# 정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

# 처음으로 다른 사람 풀이 맨 위와 일치한 문제!
# sol
a, b = map(int, input().strip().split())

print(f'a = {a}\nb = {b}')

# sol2
a, b = map(int, input().strip().split(' '))

print('a =', a)
print('b =', b)
