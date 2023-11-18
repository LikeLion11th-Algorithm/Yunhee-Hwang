# sol

n = int(input())
num = 0

for i in range(1, n+1):
    l = list(map(int, input().split()))
    num = sum(l)/10
    result = round(num)
    print(f'#{i} {result}')
