def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)#tmp는 3진법이고 이를 다시 10진수로 변환해주는 함수
    return answer

if __name__ == "__main__":

    n = 125
    print(solution(n))