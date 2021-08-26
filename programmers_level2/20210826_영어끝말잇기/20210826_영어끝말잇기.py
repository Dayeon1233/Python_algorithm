import math
def solution(n, words):
    answer = []
    duplicate_word_case = False
    wrong_word_case = False
    wrong_word_idx = -1
    duplicate_list = [words[i] for i in range(len(words)) if words.count(words[i]) > 1]
    target_list =[]

    if len(duplicate_list) > 0 :
        duplicate_word_case = True

        for word in set(duplicate_list):
            first_idx = words.index(word)
            second_idx = words.index(word,first_idx+1)
            target_list.append((first_idx, second_idx))

        sorted_target_list = sorted(target_list, key=lambda x: x[1])

        first_idx = sorted_target_list[0][0]
        second_idx = sorted_target_list[0][1]



    for i in range(len(words)-1):
        j = i+1
        lastchar = words[i][-1]
        firstchar = words[j][0]
        if lastchar != firstchar:
            wrong_word_idx = j
            wrong_word_case = True
            break

    if duplicate_word_case == False and wrong_word_case == False:
        return [0,0]

    if wrong_word_case and duplicate_word_case == False:
        return getanswer(wrong_word_idx,n)
    elif wrong_word_case == False and duplicate_word_case:
        return getanswer(second_idx,n)
    elif wrong_word_case and duplicate_word_case:
        if second_idx < wrong_word_idx:
            return getanswer(second_idx,n)
        else:
            return getanswer(wrong_word_idx,n)




def getanswer(idx,n):
    answer = []
    person = (idx % n) + 1
    cnt = (idx + 1) / n
    cnt = math.ceil(cnt)

    answer.append(person)
    answer.append(cnt)
    return answer


if __name__ == "__main__":
    n = 3
    words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

    words2 = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
    n2 = 5

    words3 = ["hello", "one", "even", "never", "now", "world", "draw"]
    n3 = 2
    print(solution(n3, words3))