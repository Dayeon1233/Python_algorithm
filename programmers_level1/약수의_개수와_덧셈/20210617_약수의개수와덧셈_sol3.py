def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        yak = set()
        for n in range(1, num//2+1):
            if num%n == 0:
                yak.add(num//n)
                yak.add(n)
        if not yak:
            yak.add(1)
        if len(yak) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer

if __name__ == '__main__':
    left = 24
    right = 27
    print(solution(left, right))


