def solution(nums):
    answer = 0
    totalSize = len(nums)

    getPocketmonSize = totalSize // 2



    my_pockeet_set = set(nums)
    my_pocket_list = list(my_pockeet_set)

    if len(my_pocket_list) <= getPocketmonSize :
        answer = len(my_pocket_list)
    else :
        answer = getPocketmonSize





    return answer


if __name__ == "__main__":
    #nums = [3,1,2,3]
    #nums = [3,3,3,2,2,4]
    nums = [3,3,3,2,2,2]
    print(solution(nums))