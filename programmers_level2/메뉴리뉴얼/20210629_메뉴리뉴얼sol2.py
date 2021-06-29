from itertools import combinations

def solution(orders, course):
    answer = []
    dict={}
    for c in course:
        for i in range(len(orders)):
           if len(orders[i]) >= c:
               combi = list(map(''.join,combinations(orders[i],c)))
               for sets in combi:

                   tmpSet = set(sets)
                   setCount = 0

                   for j in range(len(orders)):
                        tmpset2= set(orders[j])
                        if tmpSet.issubset(tmpset2):
                            setCount+=1
                   if setCount >=2:
                        sets = ''.join(sorted(sets,reverse=False))
                        dict[sets] = setCount

        if dict:
            maxval = max(dict.values())
            answer += [k for k, v in dict.items() if maxval == v]
        dict.clear()
    answer.sort()

    return answer

if __name__ == "__main__":
    #orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    #course = [2,3,4]

    #orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    #course = [2, 3, 5]

    #orders = ["XYZ", "XWY", "WXA"]
    #course = [2, 3, 4]

    orders = ["ABCD", "ABCD", "ABCD"]
    course = [2,3,4]

    print(solution(orders, course))