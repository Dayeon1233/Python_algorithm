def solution(record):
    answer = []
    nameDict = {}
    for i in record :
        tmp = i.split()
        if i.startswith("E"):
            id = tmp[1]
            nameDict[id]=tmp[2]

        elif i.startswith("C"):
            nameDict[tmp[1]] = tmp[2]

    for i in record:
        tmp = i.split()
        if i.startswith("E"):
            nickname = nameDict[tmp[1]]
            answer.append(nickname+"님이 들어왔습니다.")


        elif i.startswith("L"):
            nickname = nameDict[tmp[1]]
            answer.append(nickname + "님이 나갔습니다.")


    return answer


if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))