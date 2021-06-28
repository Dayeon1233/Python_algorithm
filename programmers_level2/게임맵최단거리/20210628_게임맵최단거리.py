from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)  # row
    m = len(maps[0])  # col

    visited = [[0]*m for i in range(n)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    q = deque()

    q.append((0,0,1))
    visited[0][0]=1


    while q:
        curR, curC, cnt = q.popleft()
        if curR == n-1 and curC == m-1:
            return cnt

        for k in range(4):
            tmpR = curR + dr[k]
            tmpC = curC + dc[k]
            if 0 <= tmpR and tmpR < n :
                if 0 <= tmpC and tmpC < m:
                    if maps[tmpR][tmpC] == 1 and visited[tmpR][tmpC] != 1:
                        q.append((tmpR,tmpC,cnt+1))
                        visited[tmpR][tmpC] = 1
    return -1

if __name__ == "__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
    print(solution(maps))