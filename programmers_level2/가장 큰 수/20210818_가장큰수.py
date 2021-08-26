# def solution(numbers):
#     #0. key point
#     numbers_str = [str(num) for num in numbers]                 #1. 사전 값으로 정렬하기
#     numbers_str.sort(key=lambda num: num*3, reverse=True)       #2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교
#
#     return str(int(''.join(numbers_str)))


import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    if int(t1) > int(t2):
        return 1
    elif int(t1) < int(t2):
        return -1
    else : return 0
   # return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer




if __name__ == "__main__":
    numbers = [383, 38]
    numbers =  [3, 30, 34, 5, 9]
    #numbers = [0,0,0,0]
    print(solution(numbers))

    #9533430
    #9534330