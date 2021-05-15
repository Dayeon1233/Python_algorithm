def solution(answers):
    answer = []
    one = 0
    two = 0
    three = 0

    setnum = 5
    pattern = [1,2,3,4,5]
    temp = calc(answers,setnum,pattern)
    max = temp
    answer.append(1)


    setnum = 8
    pattern = [2,1,2,3,2,4,2,5]
    temp = calc(answers,setnum,pattern)
    if temp > max :
        max = temp
        answer.clear()
        answer.append(2)

    elif temp == max :
        answer.append(2)


    setnum = 10
    pattern = [3,3,1,1,2,2,4,4,5,5]
    temp = calc(answers,setnum,pattern)
    if temp > max :
        max = temp
        answer.clear()
        answer.append(3)
    elif temp == max :
        answer.append(3)

    return answer

def calc(answers,setnum,pattern) :
    correct = 0
    mok = len(answers) // setnum
    namage = len(answers) % setnum

    for i in range(0,mok) :
        idx = 0
        for j in pattern :
            if j == answers[i*setnum +idx]:
                correct += 1
            idx += 1

    if namage > 0 :
        idx = 0
        for j in pattern :
            if namage > 0 :
                if j == answers[mok * setnum + idx] :
                    correct += 1
                idx += 1
                namage -= 1
    return correct



if __name__ == "__main__":
    answers=[1,3,2,4,5,4,4,3,2,2,3,4,2,1,2,3,2,2] #18
    print(solution(answers))