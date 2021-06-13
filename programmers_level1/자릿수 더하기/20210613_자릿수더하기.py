def solution(n):
    answer = 0

    strN = str(n)
    for i in strN :
        answer += int(i)



    return answer

if __name__ == "__main__":
    n=123

    print(solution(n))