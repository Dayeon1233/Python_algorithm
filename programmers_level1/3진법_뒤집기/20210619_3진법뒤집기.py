def solution(n):
    answer = 0
    ret = calcsamjinbub(n)
    retlen = len(ret)

    i = 0
    j = retlen-1
    while i<retlen :
        answer += ((3 ** i) * int(ret[j]))
        i += 1
        j -= 1
    return answer

def calcsamjinbub(n):
    ret = ''
    while n > 0:
        namage = n % 3
        n = n // 3
        ret += str(namage)
    return ret

if __name__ == "__main__":

    n = 125
    print(solution(n))