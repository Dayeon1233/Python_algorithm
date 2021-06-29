def solution(s):
    lenS = len(s)
    s = s[1:lenS-1]
    answer = []

    tmp = []
    arr=[]
    arr2=[]
    arr=s.split('},')
    for i in arr:
        tmp = []
        for j in i:
            if j.isdigit():
                tmp.append(j)
        if tmp:
            arr2.append(tmp)

    lenarr = len(arr2)
    # for i in arr:
    #     for j in i:
    #         if j.isdigit():
    #             tmp.append((j,len(i)))

    for i in arr2:
        tmp.append((i,len(i)))

    tmp = sorted(tmp, key=lambda x : x[1])

    for i in range(lenarr):
        addtarget = set()
        addtarget = set(tmp[i][0]) - set(answer)
        answer.append(addtarget.pop())

    return answer







if __name__ == "__main__":
    s = "{{20,111},{111}}"
    print(solution(s))