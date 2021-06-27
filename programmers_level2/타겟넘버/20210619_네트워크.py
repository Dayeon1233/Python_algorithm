from collections import deque
def solution(n, computers):
    answer = 0
    queue = deque()
    visited = []

    for i in computers[i] :
        for j in computers[j] :
            if computers[i][j] == 1:
                queue.append(i)
                queue.append(j)
                visited.append(i)

                bfs(queue)

    return answer
def bfs(queue):
    tmp = queue.popleft()


if __name__ == "__main__":
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    n = 3
    print(solution(n, computers))