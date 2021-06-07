def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

if __name__ == "__main__":
    # stages = [4,4,4,4,4]
    # N = 4

    stages =[2, 1, 2, 6, 2, 4, 3, 3]
    N = 5
    print(solution(N, stages))