import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >=2 :

        if scoville[0] >= K :
            return answer
        answer += 1
        min_ = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min_ + min_2*2)

    if scoville[0] >=K :
        return answer
    else:
        return -1





if __name__ == "__main__":
    scoville = [12, 9, 3, 2, 1, 10]
    K = 100
    print(solution(scoville, K))