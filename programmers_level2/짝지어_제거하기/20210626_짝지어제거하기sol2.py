def solution(n, lost, reserve):
    answer = 0

    setlost = set(lost)
    setreserve = set(reserve)

    reallost = setlost - setreserve
    lost = list(reallost)

    realresesrve = setreserve - setlost
    reserve = list(realresesrve)

    lost.sort()
    reserve.sort()

    answer = n - len(lost)
    for j in lost:
        for i in reserve :
            if j == i - 1 or j == i + 1 :
                answer += 1
                reserve.remove(i)
                break

    return answer

if __name__ == "__main__":
    #nums = [3,1,2,3]
    #nums = [3,3,3,2,2,4]
    n=3
    lost = [3]
    reserve=[1]

    print(solution(n,lost,reserve))