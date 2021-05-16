def solution(a, b):
    answer = 0
    if a<=b :
        for i in range(a,b+1) :
            answer += i
    else :
        for i in range(b,a+1) :
            answer += i


    return answer


if __name__ == "__main__":

    print(solution(5,3))