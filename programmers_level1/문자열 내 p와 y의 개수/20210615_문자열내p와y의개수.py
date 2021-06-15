def solution(s):
    answer = True
    ycnt = 0
    pcnt = 0
    for i in s :
        if i == 'y' or i =='Y' :
            ycnt += 1
        elif i =='p' or i == 'P' :
            pcnt +=1

    if ycnt == 0 and pcnt == 0:
        return True
    if ycnt == pcnt :
        return True
    else : return False



if __name__ == '__main__':
    s = "pPoooyY"
    print(solution(s))


