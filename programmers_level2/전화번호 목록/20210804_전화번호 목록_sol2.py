def solution(phone_book):
    answer = True
    phone_set = set(phone_book)
    for phone_number in phone_book :
        temp = ""
        for number in phone_number:
            temp += number
            if temp in phone_set and temp != phone_number:
                return False
    return answer



if __name__ == "__main__":
    phone_book = ["119", "97674223", "1195524421"]
    print(solution(phone_book))