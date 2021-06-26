def solution(arr):
    arrback=[]
    #arrback=arr
    arrback = sorted(arr)
    min = arrback[0]
    arr.remove(min)

    if arr :
        return arr
    else:
        arr.append(-1)
        return arr

#return [i for i in mylist if i > min(mylist)]


if __name__ == "__main__":
    arr=[10]
    print(solution(arr))