def solution(str):
     answer = ''
     word_len = len(str)
     if word_len % 2 == 0 :
         idx = word_len // 2
         print(idx)
         answer = str[idx-1] + str[idx]
         print(answer)
     else :
         idx = word_len // 2
         print(idx)
         answer = str[idx]
         print(answer)
     return answer






if __name__ == "__main__":
    str = "qwer"
    #str = "abcde"
    solution(str)