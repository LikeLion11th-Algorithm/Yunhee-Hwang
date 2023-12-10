# sol

def solution(q, r, code):
    answer = []
    for i, x in enumerate(code):
        if i % q == r:
            answer.append(x)
    return ''.join(answer)


# sol2
def solution(q, r, code):
    return code[r::q]
