from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    deq = deque(people)

    while deq:
        if len(deq) >= 2 and deq[0] + deq[-1] <= limit :
            deq.popleft()
            deq.pop()
            answer += 1

        else :
            deq.popleft()
            answer +=1
    return answer


if __name__ == "__main__":
    people = [99,80,80,19,18,5,5]
    limit = 100
    print(solution(people,limit))