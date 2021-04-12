import math

def solution(items, orderBy, orderDirection, pageSize, pageNumber):
    answer = ""
    itemlen = len(items)
    sortedList = []

    items = [[x[0], int(x[1]), int(x[2])] for x in items ]

    if orderDirection == 1 :
        sortedList=sorted(items, key = lambda items : (items[orderBy]), reverse=True)

    elif orderDirection == 0 : #오름차순
        sortedList=sorted(items, key=lambda items : (items[orderBy]))


    mock = itemlen // pageSize

    if pageNumber < mock :
        answer = [x[0] for x in sortedList[pageNumber * pageSize : (pageNumber * pageSize) + pageSize]]

    else :
        answer =[x[0] for x in sortedList[pageNumber * pageSize :]]


    return answer


if __name__ == "__main__":
    items = [['item1','10','15'],['item2','3','4'],['item3','17','8']]
    orderBy = 1
    orderDirection = 0
    pageSize = 2
    pageNumber = 1

    print(solution(items, orderBy, orderDirection, pageSize, pageNumber))