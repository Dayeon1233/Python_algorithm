def solution(str):
    l = len(str)
    if l % 2 == 0 :
        l = (l -2) // 2
        print(l)
    else :
        l = (l-1) // 2
        print(l)
    return str[int(l) : -int(l)]




if __name__ == "__main__":
    print(solution("abcd"))
    #solution(str)