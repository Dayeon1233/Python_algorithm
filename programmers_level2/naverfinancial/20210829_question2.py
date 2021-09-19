from itertools import combinations_with_replacement

def solution(A, F, M):
    # write your code in Python 3.6
    sum = 0
    nanununsu = len(A) + F

    for number in A:
        sum += number
    mid_sum = sum

    comb_list = list(combinations_with_replacement(range(1,7),F))
    for comb in comb_list:
        sum = mid_sum
        for num in comb:
            sum += num

        sum = sum // nanununsu

        if sum == M:
            return list(comb)


    return [0]




def solution(A, F, M):
    answer = []
    sum = 0
    for i in A:
        sum += i
    X = M * (len(A) + F) - sum
    if X > F * 6 or X < F:
        return [0]
    else:
        k,r = divmod(X,F)
        for i in range(0,F):
            answer.append(k)
        for i in range(0,r):
            answer[i] += 1

    return answer

if __name__ == "__main__":
    A = [3,2,4,3]
    F=2
    M=4

    A2 = [1,5,6]
    F2=4
    M2=3

    # A3 = [1,2,3,4]
    # F3 = 4
    # M3 = 6

    A3 = [6,1]
    F3 = 1
    M3 = 1

    print(solution(A3, F3, M3))