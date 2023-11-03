# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# sol
def solution(s):

    if len(s) % 2 == 1:
        return s[len(s)//2]
    else:
        return s[len(s)//2-1:len(s)//2+1]
