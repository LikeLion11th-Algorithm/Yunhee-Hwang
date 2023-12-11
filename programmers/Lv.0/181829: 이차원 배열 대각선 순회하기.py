# sol
def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i+j <= k:
                answer += board[i][j]
    return answer


# sol2
def solution(board, k):
    return sum(board[i][j] for i in range(len(board)) for j in range(len(board[i])) if i+j <= k)
