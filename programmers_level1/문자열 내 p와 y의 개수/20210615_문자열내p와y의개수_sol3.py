from collections import Counter
def solution(s):


    # 함수를 완성하세요
    c = Counter(s.lower())
    return c['y'] == c['p']


if __name__ == '__main__':
    s = "pPoooyY"
    print(solution(s))


