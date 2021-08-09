def solution(s):
    answer = ''

    arr = []
    arr = s.split(' ')
    for i in range(len(arr)):
        arr[i] = int(arr[i])


    max_num = max(arr)
    min_num = min(arr)
    answer = str(min_num) +' ' + str(max_num)
    return answer


if __name__ == "__main__":
    s = "-1 -1"
    print(solution(s))