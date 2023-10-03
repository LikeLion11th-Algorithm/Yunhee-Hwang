# 정수가 담긴 리스트 num_list가 주어집니다.
# num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

# sol
def solution(num_list):

    od = []
    ev = []

    for x in num_list:
        if x % 2 == 1:
            od.append(str(x))
        else:
            ev.append(str(x))

    if od == []:
        return int(''.join(ev))
    elif ev == []:
        return int(''.join(od))
    else:
        return int(''.join(od)) + int(''.join(ev))


# sol 정정
# 문제의 조건에 'num_list'에 적어도 한 개씩의 짝수와 홀수가 있다는 조건 있으므로 if문 처리할 필요가 없어짐

def solution(num_list):

    od = []
    ev = []

    for x in num_list:
        if x % 2 == 1:
            od.append(str(x))
        else:
            ev.append(str(x))

    return int(''.join(od)) + int(''.join(ev))

# sol2


def solution(num_list):
    a = ""  # 홀수
    b = ""  # 짝수
    for i in num_list:
        if i % 2 != 0:
            a += str(i)  # 숫자를 문자로 바꿔서 + 처리하면 바로 연결 됨
        else:
            b += str(i)
    return int(a)+int(b)
