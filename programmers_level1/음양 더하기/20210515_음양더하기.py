def solution(absolutes, signs):
    answer = 0
    lenn = len(absolutes)

    for i in range(lenn) :
        if signs[i] == True:
            answer += absolutes[i]
        else :
            answer -= absolutes[i]


    return answer

if __name__ == "__main__":
    #nums = [3,1,2,3]
    #nums = [3,3,3,2,2,4]
    absolutes=[4,7,12]
    signs=[True,False,True]

    absolutes = [1, 2, 3]
    signs = [False,False,True]


    print(solution(absolutes, signs))