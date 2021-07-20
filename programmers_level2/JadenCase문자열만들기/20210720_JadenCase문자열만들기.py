def solution(s):
    answer = []
    split = []
    length=len(s)
    j=0
    for i in range(length-1):
        if s[i] == ' ' and s[i+1] != ' ':
            split.append(s[j:i+1])
            j=i+1
    if j < i + 1:
        split.append(s[j:])

    for str in split:
        if str ==' ':
            answer.append(' ')
        elif str[0].isalpha():
            answer.append(str.capitalize())
        else:
            answer.append(str.lower())


    return ''.join(answer)

if __name__ == "__main__":
    #s= 'for the last week'
    #s = '3people unFollowed me'
    #s=' adgagd 3eagdag '
    #s='aaaaa aaa'
    s=' a   bcd  hello'

    print(solution(s))