# sol

def solution(id_list, report, k):
    new_list = []
    answer = []
    # 딕셔너리 만들기
    report_id_dic = {}  # 유저 당 신고 받은 개수 저장
    email_id_dic = {}  # 이메일 받는 개수 저장

    # 딕셔너리 각각의 value값에 숫자 0 할당
    for id in id_list:
        report_id_dic[id] = 0
        email_id_dic[id] = 0

    report = set(report)
    report = list(report)
    # report 돌면서 똑같은 사람 신고 중복 제거
    for i in range(len(report)):

        # 신고한 사람, 신고 당한 사람 배열로 저장 -> new_list: 중복 제거한 신고 배열
        a = list(report[i].split())
        new_list.append(a)

    # 신고 배열 돌면서 신고 당한 횟수 딕셔너리에 저장
    for n in new_list:
        if len(n) == 2:  # 이건 [] 제거용
            report_id_dic[n[1]] += 1
            # email_id_dic[n[0]] += 1

    # 신고 당한 거 다 저장후, k번 이상 신고된 사람 체크 -> 별
    for key, value in report_id_dic.items():
        if value >= k:
            report_id_dic[key] = '*'

    # 신고 딕셔너리 돌면서 *로 체크되어 있을 경우,
    for key, value in report_id_dic.items():
        if value == '*':
            for c in new_list:
                if c[1] == key:
                    email_id_dic[c[0]] += 1

    for value in email_id_dic.values():
        answer.append(value)

    return answer


# sol2
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
