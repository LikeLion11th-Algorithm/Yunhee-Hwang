# sol
n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())
    left = b - a
    right = c - b
    if (b-a) == (c-b):
        print(f'#{i + 1} {0.0}')

    else:
        print(f'#{i + 1} {abs((right - left) / 2)}')
