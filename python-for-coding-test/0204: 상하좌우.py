# 구현 문제, 문제는 노션에서 확인

# 초기 풀이
# 0이하 혹은 n 이상이 될 때를 구현하지 못함
n = int(input())

direction = list(map(str, input().split()))

x, y = 1, 1

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

while 0 <= x <= n and 0 <= y <= n:
    for i in direction:
        if i == "R":
            x = x + dx[0]
            y = y + dy[0]
        if i == "U":
            x = x + dx[1]
            y = y + dy[1]
        if i == "L":
            x = x + dx[2]
            y = y + dy[2]
        if i == "D":
            x = x + dx[3]
            y = y + dy[3]

        print(x, y)


# sol - example
# N 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()  # 그냥 이렇게 해도 배열로 처리되는군

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        nx = x + dx[i]
        ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
