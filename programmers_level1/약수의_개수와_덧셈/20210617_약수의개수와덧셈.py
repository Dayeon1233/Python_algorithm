def solution(left, right):
    answer = 0
    for i in range(left, right+1) :
        numofyaksu = yaksu(i)
        if numofyaksu % 2 == 0 :
            answer += i
        else : answer -= i


    return answer
def yaksu(i) :
    num = 0
    for j in range(1, i+1) :
        if i % j == 0 :
            num +=1
    return num

if __name__ == '__main__':
    left = 24
    right = 27
    print(solution(left, right))


