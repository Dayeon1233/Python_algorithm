import math

def solution(s):
    answer = ""
    length = len(s)
    answerlen  = 999999

    for i in range(1,length+1) :
        answer = ""
        j = 0
        cnt = 0
        str = ""
        prestr = s[j:j+i]

        while j+i <= length :
            str = s[j : i+j]

            if str == prestr :
                if s.startswith(str,j) :
                    cnt +=1
                    j+=i
                    prestr = str

            else :
                if cnt != 1 :
                    answer += repr(cnt)
                answer += prestr
                cnt = 1
                prestr = str
                j += i

        if cnt != 1:
            answer += repr(cnt)
        namage  = s[(j-i):]
        answer += namage

        tmpanswerlen = len(answer)
        if tmpanswerlen < answerlen :
            answerlen = tmpanswerlen
    return answerlen


if __name__ == "__main__":
    s = "xababcdcdababcdcd"
    print(solution(s))