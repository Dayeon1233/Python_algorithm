def solution(n, arr1, arr2):
    import re
    fin_list=[]
    for i in range(len(arr1)):
        fin_list.append(str(int(bin(arr1[i])[2:])+int(bin(arr2[i])[2:])).zfill(n))
        fin_list[i]=re.sub('[^0]','#',fin_list[i])
        fin_list[i]=re.sub('0', ' ',fin_list[i])
    return fin_list


if __name__ == "__main__":
    n=5
    arr1 = 	[9, 20, 28, 18, 11]
    arr2 = 	[30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))