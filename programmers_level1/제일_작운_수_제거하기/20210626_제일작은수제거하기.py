def solution(s):#baabaa
    index = 0
    lists = []
    lists = list(s)
    initlenS = len(lists)

    while True:
        lenS = len(lists) #6

        if lenS == 0:
            return 1
        elif lenS > 0 and (index == initlenS-1 or index == 0):
            return 0
        #elif index == initlenS -1

        else:
            for i in range(0,lenS-1):
                if lists[i] == lists[i+1]:
                    tmp = lists[i]
                    lists.remove(tmp)
                    lists.remove(tmp)
                    index += i+1 #4
                    break;


#2 3 4

if __name__ == "__main__":
    s = "baabaa"
    print(solution(s))