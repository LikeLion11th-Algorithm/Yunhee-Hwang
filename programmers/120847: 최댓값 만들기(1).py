#정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

#sol
def solution(numbers):
    #오름차순 정렬
    numbers.sort()
    #리스트 맨 끝 숫자와 그 전 숫자 곱
    answer= numbers[len(numbers)-1]*numbers[len(numbers)-2]
    return answer