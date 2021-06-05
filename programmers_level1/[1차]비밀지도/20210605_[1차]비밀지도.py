def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        rowAarr1 = tenToTwo(n,arr1[i])
        rowArr2 = tenToTwo(n,arr2[i])
        rowAnswer = ""
        for j in range(n) :
            if rowArr1[j] == 1 :
                rowAnswer += '#'
            else :
                if rowArr2[j] == 1 :
                    rowAnswer += '#'
                else :
                    rowAnswer += " "
        answer.append(rowAnswer)

    return answer

def tenToTwo(n,num) :
    ret = []
    while num != 0 :
        ret.append(num % 2)
        num //=2
    if len(ret) < n :
        ret += [0] * (n - len(ret))
    ret.reverse()
    return ret


if __name__ == "__main__":
    n=5
    arr1 = 	[9, 20, 28, 18, 11]
    arr2 = 	[30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))