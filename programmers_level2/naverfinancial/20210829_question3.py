# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import heapq
def solution(N):
    answer = 0
    heap = []
    for i in range(0,201):
        P = 2**i
        for j in range(0,201):
            Q = 3**j
            heapq.heappush(heap,P*Q)

    for i in range(0, N+1):
        answer = heapq.heappop(heap)

    # print(answer)
    return answer


if __name__ == "__main__":

    print(solution(5))