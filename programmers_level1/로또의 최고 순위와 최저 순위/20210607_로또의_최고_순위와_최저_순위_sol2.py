def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]


if __name__ == "__main__":
    lottos = [1, 2, 3, 4, 5, 6]
    win_nums =	[38, 19, 20, 40, 15, 25]
    print(solution(lottos, win_nums))