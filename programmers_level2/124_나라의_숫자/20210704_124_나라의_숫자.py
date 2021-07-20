from collections import deque
def solution(n):
    global dict,ans,tmp
    ans = deque()
    tmp = []
    answer = calc1(n,ans,tmp)

    return str(answer)

def calc1(n,ans,tmp):
    dict = {1: '1', 2: '2', 3: '4', 4: '11', 5: '12', 6: '14', 7: '21', 8: '22', 9: '24', 10: '41'}
    if n <= 10:
        return dict[n]

    elif n % 3 == 1:
        baggi = 3
    elif n % 3 == 2:
        baggi = 2
    else:
        baggi = 0
    calc2(n,ans,tmp)
    answer = ''.join(ans)
    return int(answer) - baggi

def calc2(n,ans,tmp):
    if n<=10:
        ret = dict[n]
        ans.appendleft(dict[n])
        return ans

    elif n % 3 == 0:
        su = n // 3 - 1

    elif n % 3 ==1:
        su = (n +2)//3 -1

    elif n % 3==2:
        su = (n + 1) // 3 - 1

    if su>10:
        calc2(su,ans,tmp)

    aa = calc1(su,ans,tmp)
    tmp.append(aa)
    return ans





if __name__ == "__main__":
    n = 36
    print(solution(n))