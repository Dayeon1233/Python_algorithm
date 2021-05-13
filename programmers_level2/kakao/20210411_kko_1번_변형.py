#O(N)
def solution(arr):
    print("arr" ,arr)
    per = {}
    answerdict = {}
    answer = []
    min = 0

    for i in arr:
        if i[0] not in per:
            per[i[0]] = -int(i[2])
        else:
            per[i[0]] = per[i[0]] - int(i[2])

        if per[i[0]] < min :
            min = per[i[0]]
            answerdict = {}
            answerdict[i[0]] = min
        elif per[i[0]] < 0 and per[i[0]] == min :
            answerdict[i[0]] = min


        if i[1] not in per:
            per[i[1]] = int(i[2])
        else:
            per[i[1]] = per[i[1]] + int(i[2])

        if i[1] in answerdict:
            if min < per[i[1]]:
                answerdict.pop(i[1])

                if len(answerdict) == 0 :
                    min = 0


    answer = answerdict.keys()
    answer = list(answer)

    if len(answer) == 0:
        answer.append("None")
    answer.sort()  # O(N Log N)


# 최악 또는 평균의 경우 O(N Log N)
# 최고의 경우 O(N)

    return answer



if __name__ == "__main__":
    arr = [
        ['Frodo', 'Apeach', 7],
        ['Frodo', 'Apeach', 3],
        ['Apeach', 'Frodo', 4],
        ['Frodo', 'Apeach', 1],
        ['Apeach', 'Frodo', 7]
    ]
    #None
    # arr=[
    #    ['Neo', 'Tube', 12],
    #    [ 'Muzi', 'Tube', 18],
    #    [ 'Neo', 'Tube', 5],
    #    [ 'Neo', 'Frodo', 17],
    #    [ 'Neo', 'Frodo', 8],
    #    [ 'Neo', 'Muzi', 6],
    #    [ 'Tube', 'Muzi', 8],
    #    [ 'Tube', 'Frodo', 1],
    #     [ 'Tube', 'Muzi', 5],
    #     ['Frodo', 'Tube', 6]
    # ]
    # Neo
    # Neo
    # Neo
    # Neo
    # Neo

    print(solution(arr))