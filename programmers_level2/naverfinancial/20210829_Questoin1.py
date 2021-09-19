from collections import deque
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import combinations
def solution(S):
    for idx in range(len(S)):
        if S[idx]


def solution(S):
    answer = S[1:]
    for idx in range(2, len(S)+1):
        tempString = S[:idx-1] + S[idx:]
        # print(idx,tempString)
        if answer > tempString:
            answer = tempString
    # print(answer)
    return answer

if __name__ == "__main__":
    print(solution("codility"))