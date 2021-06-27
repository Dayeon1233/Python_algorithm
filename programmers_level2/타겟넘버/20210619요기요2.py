def solution(S):
    # write your code in Python 3.6
    global lenS
    global fixAcnt
    global setanswer
    lenS = len(S)
    cntA = S.count('a')
    answer = 0
    nowAcnt = 0
    splitarr = []
    setanswer = set()
    if cntA % 3 != 0 and cntA != 0 :
        return 0

    else:
        fixAcnt = cntA // 3
        for i in range(0, lenS):
            if S[i] == 'a':
                nowAcnt += 1
                if nowAcnt == fixAcnt:
                    splitarr.append(S[0:i+1])
                    calca(S[i+1:], i, splitarr)
                    secondAIndex = S.find('a', i + 1)
                    if secondAIndex != -1:
                        splitarr.append(S[0:secondAIndex+1])
                        calca(S[secondAIndex+1:], secondAIndex, splitarr)


   #elif cntA == 0:


    return len(setanswer)

def calca(S,totalIndex,splitarr) :

    if S.count('a') == fixAcnt:
        splitarr.append(S)
        return splitarr
    elif S.count('a') < fixAcnt:
        return splitarr
    elif totalIndex == lenS :
        return splitarr
    for i in range(0,len(S)):

        if S[i] == 'a':
            secondAIndex = S.find('a', i + 1)
            splitarr.append(S[0:i+1])
            setanswer.add(calca(S[i+1:], totalIndex+i+2, splitarr))

    return splitarr

if __name__ == "__main__":
    S = 'babaa'
    print(solution(S))