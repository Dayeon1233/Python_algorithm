def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    size = len(citations)

    if citations[-1] > size :
        return size
    for idx in range(size):
        if idx + 1 == citations[idx]:
            answer = idx + 1
            break
        elif idx + 1 > citations[idx]:
            answer = idx
            break

    return answer




if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    citations2 = [4,4,4,4,4,1,1,1]
    citations3 = [1,3,3,3,4,4,4,4,4]
    citations4 = [4,4,3,2,1]
    citations5 = [9,9, 2, 1]
    citations6 = [9,9,8,8,8,6,6,6,6,4,4,2]
    citations7 = [1,0,0,0]
    citations8 = [12,11,10,9,8,1]
    print(solution(citations))
