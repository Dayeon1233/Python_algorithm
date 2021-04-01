from math import ceil

def solution(progresses, speeds):
    daysLeft = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    print("daysLeft",daysLeft)
    count = 1
    retList = []

    for i in range(len(daysLeft)):
        try:
            if daysLeft[i] < daysLeft[i + 1]:
                retList.append(count)
                count = 1
            else:
                daysLeft[i + 1] = daysLeft[i]
                count += 1
        except IndexError:
            retList.append(count)

    return retList

if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))