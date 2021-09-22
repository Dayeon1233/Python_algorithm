# def solution(skill, skill_trees):
#     answer = 0
#
#     for skills in skill_trees:
#         skill_list = list(skill)
#
#         for s in skills:
#             if s in skill:
#                 if s != skill_list.pop(0):
#                     break
#         else:
#             answer += 1
#
#     return answer


# def solution(skill,skill_tree):
#     answer=0
#     for i in skill_tree:
#         skillist=''
#         for z in i:
#             if z in skill:
#                 skillist+=z
#         if skillist==skill[0:len(skillist)]:
#             answer+=1
#     return answer


# def solution(skill, skill_trees):
#     def check(skill,branch):
#         branch=list(filter(lambda x:x in skill,branch))
#         checked=0
#         for b in branch:
#             if skill[checked]==b:
#                 checked=checked+1
#             else:
#                 return 0
#         return 1
#
#
#     return sum(list(map(lambda x: check(skill, x), skill_trees)))


def solution(skill, skill_trees):
    b = ''.join([s for s in list('BDA') if s in skill])
    a = skill.find(b) == 0
    lists = list(filter(lambda st: skill.find(''.join([s for s in list(st) if s in skill])) == 0, skill_trees))
    return len(list(filter(lambda st:skill.find(''.join([s for s in list(st) if s in skill]))==0, skill_trees)))






if __name__ == "__main__":
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    skill = "CBD"
    print(solution(skill, skill_trees))

    # cbd 에서 d부터, 뒤쪽부터 for문으로 돌리면서 인덱스순서가 제대로 인지 검사,
    # 제일 첫번째 글자가 d일경우 b일 경우 그런걸 first로 고정해놓고,,,돌다가 중간껄 건너뒤꺼나 d,b만 있고 c가 없는 경우는
    # 제대로된 순서가 아님을 구현하려고 하다 말앗음
