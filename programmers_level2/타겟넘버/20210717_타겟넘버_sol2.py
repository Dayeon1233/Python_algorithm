from collections import deque
answer = 0
def solution(numbers, target):

    #global target2 = target
    dfs(numbers[0],0, numbers, target)
    dfs(-1*numbers[0],0, numbers, target)

    return answer

def dfs(calc,cnt, numbers, target):
    if cnt == len(numbers)-1 :
        if calc == target :
            global answer
            answer = answer + 1
            return
        return

    cnt = cnt + 1
    tmp = numbers[cnt]
    dfs(calc + numbers[cnt],cnt,numbers, target)
    dfs(calc - numbers[cnt],cnt,numbers, target)
    return
if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1],3))