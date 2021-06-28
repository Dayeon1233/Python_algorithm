from collections import deque
def solution(priorities, location):
    answer = 0
    cnt=0
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i],i))


    while q:
        thisMax = max(q)
        first = q[0]
        if first[0] <thisMax[0]:
            first = q.popleft()
            q.append(first)
        else:
            cnt+=1
            item = q.popleft()
            if item[1] == location:
                return cnt



# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer



if __name__ == "__main__":
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))