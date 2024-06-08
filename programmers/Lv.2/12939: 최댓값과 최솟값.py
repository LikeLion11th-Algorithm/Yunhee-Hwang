# sol1
def solution(s):
    l = s.split(' ')
    l = list(map(int, l))
    print(l)
    return str(min(l))+' '+str(max(l))


# sol2
def solution(s):
    l = list(map(int, s.split(' ')))
    l = [str(min(l)), str(max(l))]
    return (" ".join(l))
