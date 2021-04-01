import math

def solution(progresses,speeds):
    answer = []
    length = len(progresses)
    q = []
    for i in range(length) :
        day = (100-progresses[i]) / speeds[i]
        day = math.ceil(day)
        q.insert(0,day)

    cnt = 1
    top = q.pop()

    answer = calc(q, top, cnt, answer)

    return answer


def calc(q, top, cnt, answer) :
        if q :
            temp = q.pop()
            if temp <= top :
                cnt+=1
                calc(q,top,cnt,answer)
            else :
                answer.append(cnt)
                cnt = 1
                calc(q,temp,cnt,answer)

        else :
            answer.append(cnt)

        return answer;



if __name__ == "__main__":
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    #numbers = [5,0,2,7]
    print(solution(progresses,speeds))