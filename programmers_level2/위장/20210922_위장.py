from functools import reduce
from itertools import combinations

def multiply(arr):
    return reduce(lambda x, y: x * y, arr)

def solution(clothes):
    clothes_hash = {}
    for clothe in clothes:
        if clothe[1] in clothes_hash :
            clothes_hash[clothe[1]] +=1
        else :
            clothes_hash[clothe[1]] = 1

    if len(clothes_hash) == 1:
        return len(clothes)
    else:
        sum = 0
        values = []
        for i in clothes_hash.values():
            values.append(i+1)
        sum += multiply(values) #모든 종류의 옷을 입는 경우임
        sum -= 1

        return sum


if __name__ == "__main__":
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"],["blue_pants", "pants"]]
    clothes2 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"],
               ]
    #clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(clothes2))


    # def solution(clothes):
    #     clothes_hash = {}
    #     for clothe in clothes:
    #         if clothe[1] in clothes_hash:
    #             clothes_hash[clothe[1]] += 1
    #         else:
    #             clothes_hash[clothe[1]] = 1
    #
    #     if len(clothes_hash) == 1:
    #         return len(clothes)
    #     else:
    #         sum = 0
    #         values = list(clothes_hash.values())
    #         sum += multiply(values)  # 모든 종류의 옷을 입는 경우임
    #         for num in values:  # 한 종류의 옷만 입는 경우임
    #             sum += num
    #
    #         for r in range(2, len(clothes_hash)):
    #             comb_list = list(combinations(clothes_hash, r))
    #             for comb in comb_list:
    #                 target_list = []
    #                 for clothe in comb:
    #                     target_list.append(clothes_hash[clothe])
    #                 sum += multiply(target_list)
    #         return sum