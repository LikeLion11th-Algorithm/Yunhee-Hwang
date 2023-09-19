# 문자열 str과 정수 n이 주어집니다.
# str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

# sol
a, b = input().strip().split(' ')
b = int(b)

string = ''

for i in range(b):
    string += a

print(string)

# sol2
a, b = input().strip().split(' ')
b = int(b)

result = a * b  # 문자열 * 정수 하면 문자열이 정수배만큼 반복된다
print(result)
