def solution(prices):
    answer = []
    prices_len = len(prices)
    answer.append(0)

    for i in range(prices_len-2,-1,-1):
        for j in range(i+1,prices_len):
            price_down = False
            if prices[i] > prices[j]: #가격이 떨어짐
                answer.append(j-i)
                price_down = True
                break
        if price_down == False :
            answer.append(j-i)
    return list(reversed(answer))



if __name__ == "__main__":
    #prices = [1,2,3,2,3,1]
    #prices = [1, 2, 3, 2, 3]
    prices = [1,2,3,3,2]
    print(solution(prices))