def solution(bricks):

	answer = 0
	n = len(bricks)

	left_max_heights = [0] * n
	right_max_heights = [0] * n

	left_max = 0
	for i in range(n):
	    left_max = max(left_max, bricks[i])
	    left_max_heights[i] = left_max

	right_max = 0
	for i in range(n - 1, -1, -1):
	    right_max = max(right_max, bricks[i])
	    right_max_heights[i] = right_max

	for i in range(1, n - 1):
	    min_height = min(left_max_heights[i], right_max_heights[i])
	    if min_height > bricks[i]:
	        answer += min_height - bricks[i]
    return answer