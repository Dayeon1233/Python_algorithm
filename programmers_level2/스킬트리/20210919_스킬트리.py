def solution(skill, skill_trees):
    answer = 0
    for user_skill in skill_trees :
        now_idx = 27
        is_right = True
        first = False

        for idx in range(len(skill)-1,-1,-1):
            if user_skill.count(skill[idx]) > 0:
                first = True
                tmp_idx = user_skill.index(skill[idx])
                if now_idx > tmp_idx:
                    now_idx = tmp_idx
                else :
                    is_right = False
                    break
            else :
                if first == True :
                    is_right = False

        if is_right:
            answer += 1
    return answer






if __name__ == "__main__":
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    skill = "CBD"
    print(solution(skill, skill_trees))

    # cbd 에서 d부터, 뒤쪽부터 for문으로 돌리면서 인덱스순서가 제대로 인지 검사,
    # 제일 첫번째 글자가 d일경우 b일 경우 그런걸 first로 고정해놓고,,,돌다가 중간껄 건너뒤꺼나 d,b만 있고 c가 없는 경우는
    # 제대로된 순서가 아님을 구현하려고 하다 말앗음
