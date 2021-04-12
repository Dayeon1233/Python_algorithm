import math

from collections import deque

def solution(numbers, target):
    answer = 0
    # stack = collections.deque([(0, 0)])
    # print("stc",stack)
    # print("")
    # while stack:
    #     current_sum, num_idx = stack.popleft()
    #
    #     if num_idx == len(numbers):
    #         if current_sum == target:
    #             answer += 1
    #     else:
    #         number = numbers[num_idx]
    #         stack.append((current_sum+number, num_idx + 1))
    #         stack.append((current_sum-number, num_idx + 1))
    stack = deque()
    print("stc", stack)

    return answer


if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1],3))