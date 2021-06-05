def solution(numbers, hand):
    answer = []
    leftThumb = [-1,3,0]
    rightThumb = [-1,3,2]
    dial = [(0,3,1),(1,0,0),(2,0,1),(3,0,2),(4,1,0),(5,1,1),(6,1,2),(7,2,0),(8,2,1),(9,2,2)]

    for i in  numbers :
        if i in [1,4,7] :
            leftThumb = dial[i]
            answer.append("L")
        elif i in [3,6,9] :
            rightThumb = dial[i]
            answer.append("R")
        else :
            row = dial[i][1]
            col = dial[i][2]

            leftDistance = abs(leftThumb[1]-row ) + abs(leftThumb[2]-col)
            rightDistance = abs(rightThumb[1]-row) + abs(rightThumb[2]-col)
            if leftDistance > rightDistance :
                rightThumb = dial[i]
                answer.append("R")
            elif leftDistance < rightDistance :
                leftThumb = dial[i]
                answer.append("L")
            else :
                if hand.startswith("l") :
                    leftThumb = dial[i]
                    answer.append("L")
                else :
                    rightThumb = dial[i]
                    answer.append("R")

    answer = "".join(answer)
    return answer

if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand = "right"
    print(solution(numbers, hand))