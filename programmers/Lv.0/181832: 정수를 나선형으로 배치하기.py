# sol
def solution(n):
    answer = [[0 for x in range(n)] for _ in range(n)]
    row = n
    col = n
    x_idx, y_idx = 0, 0
    direction = "right"

    for i in range(1, (n*n+1)):
        answer[x_idx][y_idx] = i

        if direction == "right":
            if y_idx+1 == n or answer[x_idx][y_idx+1] != 0:
                direction = "down"
                x_idx += 1
            else:
                y_idx += 1

        elif direction == "down":

            if x_idx+1 == n or answer[x_idx+1][y_idx] != 0:
                direction = "left"
                y_idx -= 1
            else:
                x_idx += 1

        elif direction == "left":
            if answer[x_idx][y_idx-1] != 0:
                direction = "up"
                x_idx -= 1
            else:
                y_idx -= 1

        elif direction == "up":
            if answer[x_idx-1][y_idx] != 0:
                direction = "right"
                y_idx += 1
            else:
                x_idx -= 1
    return answer
