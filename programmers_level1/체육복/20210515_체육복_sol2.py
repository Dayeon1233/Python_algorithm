def solution(n, lost, reserve):
    answer = 0

    n = [1 for x in range(n)]

    for l in lost:
        n[l - 1] -= 1
    for r in reserve:
        n[r - 1] += 1

    for i in range(len(n) - 1, -1, -1):
        if n[i] == 0:
            if i + 1 <= len(n)-1 and n[i + 1] == 2:
                n[i] = 1
                n[i + 1] = 1

    for i in range(len(n)):
        if n[i] == 0:
            if i - 1 >= 0 and n[i - 1] == 2:
                n[i] = 1
                n[i - 1] = 1
    answer = len([x for x in n if x != 0])
    # answer = n
    return answer
if __name__ == "__main__":
    #nums = [3,1,2,3]
    #nums = [3,3,3,2,2,4]
    n=3
    lost = [3]
    reserve=[1]

    print(solution(n,lost,reserve))