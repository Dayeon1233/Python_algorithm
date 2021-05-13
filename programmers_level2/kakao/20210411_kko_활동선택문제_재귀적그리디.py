#O(N)

def solution(start_time, running_time):

    timeLen = len(start_time)
    endtime = []
    for i in range(timeLen) :
        endtime.append(start_time[i]+running_time[i])
    pairlist = list(zip(start_time,endtime))
    pairlist.sort(key = lambda x:(x[1],x[0]))
    k = 0
    cnt = 1
    return recur(pairlist, k, timeLen,cnt)

def recur (pairlist, k, timeLen, cnt) :

    m = k + 1
    banbok = 1
    while m < timeLen and pairlist[m][0] < pairlist[k][1]:
        m = m + 1
        banbok += 1
    if m < timeLen:
        cnt += 1
        k += banbok
        return recur(pairlist, k, timeLen, cnt);
    else :
        return cnt



if __name__ == "__main__":
    # start_time = [978, 490, 229, 934, 299, 982, 636, 14, 866, 815, 64, 537, 426, 670,
    #               116, 95, 630]
    # running_time = [502, 518, 196, 106, 405, 452, 299, 189, 124, 506, 883, 753, 567,
    #                 717, 338, 439, 145]
    # 4

    start_time = [1, 3, 3, 5, 7]
    running_time = [2, 2, 1, 2, 1]
    # 4

    # start_time = [1]
    # running_time = [1]
    # 1

    # start_time = [1, 3, 5]
    # running_time = [2, 2,2]
    # 3
    print(solution(start_time, running_time))