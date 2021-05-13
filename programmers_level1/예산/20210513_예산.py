from collections import deque
from itertools import combinations

def solution(d, budget):
    answer = 0
    d.sort()

    cnt = 0
    for i in d :
        cnt += i
        if cnt > budget :
            break
        else :
            answer += 1

    return answer


if __name__ == "__main__":
    d=[2,2,3,3]
    budget = 10
    print(solution(d, budget))