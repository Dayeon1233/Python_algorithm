from itertools import combinations
def solution(nums):
    answer = 0

    combi = list(combinations(nums,3))
    for i in combi :
        if is_prime_number(sum(i)) :
            answer +=1
    return answer

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

if __name__ == '__main__':
    nums = [1,2,7,6,4]
    print(solution(nums))


