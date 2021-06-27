# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    answer = 0
    arr = S.split('\n')
    #arr.remove('')
   # arr.remove(' ')
    minFileSize = 240 * 2**10
    Month = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}


    for i in arr :
        column = i.split()
        filesize = int(column[0])
        if filesize >= minFileSize :
            if int(column[3]) == 1990 :
                if Month[column[2]] > 1 :
                   # if column[4].count('.') >= 1 and len(column[4]) <= 255 :
                        answer += 1

            elif int(column[3]) > 1990 :
                #if column[4].count('.') >= 1 and len(column[4]) <= 255:
                    answer += 1
    if answer == 0 :
        return 'NO FILES'


    return str(answer)



if __name__ == "__main__":


    S=' 779091968 23 Sep 2009 system.zip\n 284164096 14 Aug 2013 to-do-list.xml\n 714080256 19 Jun 2013 blockbuster.mpeg\n       329 12 Dec 2010 notes.html\n 444596224 17 Jan 1950 delete-this.zip\n       641 24 May 1987 setup.png\n    245760 16 Jul 2005 archive.zip\n 839909376 31 Jan 1990 library.dll'
    #사이즈는 길이 10 2^31바이트 사이즈는  --> 240 * 2^10바이트보다 크거나 같아야 함
    # 31 Jan 1990 보다 커야 함
    #최대 255 프린터블할 아스키 캐릭터 최소 하나이상의 점
    print(solution(S))