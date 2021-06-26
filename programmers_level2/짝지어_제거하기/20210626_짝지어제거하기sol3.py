from collections import deque

def solution(s):#baabaa
    q = deque(s)
    lists=list(s)
    index = 0
    initLen = len(s)
    while q:
        for i in range(0,len(q)-1):
            if q[i] == q[i+1]:
                tmp = q[i]
                q.remove(tmp)
                q.remove(tmp)
                index += i+1
                break;
            else:
                index = i
        if q and index == initLen-2:
            return 0

    return 1



if __name__ == "__main__":

    s="baabaa"

    print(solution(s))