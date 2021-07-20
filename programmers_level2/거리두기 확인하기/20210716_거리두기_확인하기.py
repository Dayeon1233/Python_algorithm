from itertools import combinations
def solution(places):
    answer = []

    p_collect=[]
    for pan in places:
        p_collect = []
        for r in range(5):#POOOP
            for c in range(5):
                if pan[r][c] == 'P':
                    p_collect.append((r,c))

        combi = list(combinations(p_collect,2))
        flag = 1
        for i in combi:
            location1 = i[0]
            location2 = i[1]
            distance = calc_distance(location1,location2)
            if distance ==2:
                if location1[0] == location2[0] :
                    c = (location1[1]+location2[1])//2
                    if pan[location1[0]][c] == 'O':
                        answer.append(0)
                        flag = 0
                        break
                elif location1[1] == location2[1] :
                    r = (location1[0] + location2[0]) // 2
                    if pan[r][location1[1]] == 'O':
                        answer.append(0)
                        flag = 0
                        break
                elif pan[location1[0]][location2[1]] == 'O' or pan[location1[1]][location2[0]] == 'O':
                    answer.append(0)
                    flag = 0
                    break
            elif distance < 2:
                answer.append(0)
                flag = 0
                break
        if flag == 1:
            answer.append(1)
    return answer


def calc_distance(location1,location2):
    distance = abs(location1[0] - location2[0]) + abs(location1[1] - location2[1])
    return distance







if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))