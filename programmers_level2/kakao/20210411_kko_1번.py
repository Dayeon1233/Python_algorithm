
def solution(arr):
    print("arr" ,arr)
    per = {}
    answer = []
    min = 0
    for i in arr:
        if i[0] not in per:
            per[i[0]] = -int(i[2])
        else:
            per[i[0]] = per[i[0]] - int(i[2])
        if i[1] not in per:
            per[i[1]] = int(i[2])
        else:
            per[i[1]] = per[i[1]] + int(i[2])

    for j in per:
        if per[j] < min:
            min = per[j]
            answer = []
            answer.append(j)
        elif per[j] < 0 and per[j] == min:
            answer.append(j)
    if len(answer) == 0:
        answer.append("None")

    answer.sort()

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
    arr=[
       ['Neo', 'Tube', 12],
       [ 'Muzi', 'Tube', 18],
       [ 'Neo', 'Tube', 5],
       [ 'Neo', 'Frodo', 17],
       [ 'Neo', 'Frodo', 8],
       [ 'Neo', 'Muzi', 6],
       [ 'Tube', 'Muzi', 8],
       [ 'Tube', 'Frodo', 1],
        [ 'Tube', 'Muzi', 5],
        ['Frodo', 'Tube', 6]
    ]
    # Neo
    # Neo
    # Neo
    # Neo
    # Neo

    print(solution(arr))