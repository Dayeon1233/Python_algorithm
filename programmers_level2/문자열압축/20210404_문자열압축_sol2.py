def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    print("")
    print("토크렌!!tok_len=", tok_len)
    print("words=",words)
    res = []
    cur_word = words[0]
    print("cur_word=", cur_word)
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        print("words         =", words)
        print("words[1:] + ['']",words[1:] + [''])
        print("a=",a)
        print("b=", b)
        if a == b:
            cur_cnt += 1
            print("if cur_cnt=", cur_cnt)
        else:
            res.append([cur_word, cur_cnt])
            print("res",res)
            cur_word = b
            cur_cnt = 1

    print("뿌린트",sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res))
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
#tok_len은 1~4까지
    # for i in range(1, int(len(text) / 2) + 1):
    #     print("")
    #     print(i)
    #     print(int(len(text) / 2) + 1)
    # return min( print("tok_len",tok_len) for tok_len in list(range(1, int(len(text) / 2) + 1)) + [len(text)])


if __name__ == "__main__":
    a = [
        "aabbaccc"#길이 8
        # ,"ababcdcdababcdcd",
        # "abcabcdede",
        # "abcabcabcabcdededededede",
        # "xababcdcdababcdcd",
        # 'aaaaaa',
    ]

    for x in a:
        solution(x)
        # print(solution(x))