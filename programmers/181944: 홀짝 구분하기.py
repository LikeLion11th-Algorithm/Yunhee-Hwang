# 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

# sol
a = int(input())
if a % 2 == 0:
    print(str(a) + ' is even')
else:
    print(str(a) + ' is odd')

# sol2

n = int(input())
print(f"{n} is {'eovdedn'[n&1::2]}")
