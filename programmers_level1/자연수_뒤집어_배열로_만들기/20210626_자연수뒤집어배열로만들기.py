def solution(n):
    answer = []
    strn = str(n)
    lenN=len(strn)
    for i in range(lenN-1,-1,-1):
        answer.append(int(strn[i]))
    return answer
if __name__ == "__main__":
    n=12345

    print(solution(n))