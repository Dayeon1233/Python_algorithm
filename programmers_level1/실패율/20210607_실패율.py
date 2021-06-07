def solution(N, stages):
    answer = []
    check = {}
    check[N+1]=True
    totalTry = [0] * (N+2)

    stages.sort()
    for i in stages :
        totalTry[i]+=1

    for i in stages :
        if i not in check :
            cntI = stages.count(i)
            totaluser = 0
            j = i
            for j in range(j,N+2) :
                totaluser += totalTry[j]
            answer.append((i,cntI/totaluser))
            check[i]=True


    for i in range(1,N+1) :
        if i not in check :
            answer.append((i,0.0))

    answer2 = [x[0] for x in sorted(answer, key = lambda x : (-x[1],x[0]))]

    return answer2

if __name__ == "__main__":
    stages = [4,4,4,4,4]
    N = 4
    print(solution(N, stages))