import math


def solution(w,h):
    gcd = math.gcd(w,h)
    naw = w// gcd
    nah = h//gcd

    return w*h - (naw + nah -1) * gcd

    #return w*h-w-h+gcd(w,h)

# 8 12 4
if __name__ == "__main__":
    W = 8
    H = 12
    print(solution(W,H))