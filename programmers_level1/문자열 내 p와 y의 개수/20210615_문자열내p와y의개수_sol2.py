def solution(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')



if __name__ == '__main__':
    s = "pPoooyY"
    print(solution(s))


