def solution(number, k):

    make_number = ''
    make_max_number = -1

    total_len = len(number)
    cnt = total_len - k

    max_num_digit = -1
    max_num_idx = -1
    for idx in range(0,cnt+1):
        if int(number[idx]) > max_num_digit:
            max_num_digit = int(number[idx])
            max_num_idx = idx

    make_number += str(max_num_digit)


    def calc(make_number, idx,make_max_number):
        if len(make_number) == cnt:
            if int(make_number) > make_max_number:
                make_max_number = int(make_number)
            return make_max_number

        if idx >= total_len:
            return make_max_number
        else :
            tmp1 = calc(make_number + number[idx], idx+1,make_max_number)
            if make_max_number < tmp1 :
                make_max_number = tmp1
            tmp2 = calc(make_number, idx+1,make_max_number)
            if make_max_number < tmp2 :
                make_max_number = tmp2
        return make_max_number


    make_max_number = calc(make_number,max_num_idx+1,make_max_number)

    return str(make_max_number)


if __name__ == "__main__":
    #number1 = "1924"
    number2 = "1231234"
    number3 = "4177252841"
    k1 = 2
    k2 = 3
    k3 = 4
    print(solution(number3, k3))