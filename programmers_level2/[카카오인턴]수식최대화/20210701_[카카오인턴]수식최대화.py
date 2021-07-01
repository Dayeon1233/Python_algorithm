from collections import deque
from itertools import permutations
import copy
def solution(expression):
    answer=[]

    ex_list = deque()

    operator = set()
    tmp_num = ''
    for i in expression:
        if i.isdigit():
            tmp_num+=i
        else :
            ex_list.append(int(tmp_num))
            tmp_num = ''
            ex_list.append(i)
            operator.add(i)

    ex_list.append(int(tmp_num))
    permu_list=list(map(''.join, permutations(operator)))

    for permu in permu_list:
        ex_list_copy = copy.deepcopy(ex_list)
        for i in permu:
            while ex_list_copy.count(i) > 0:
                calc_result = 0

                idx = ex_list_copy.index(i)
                operand1 = ex_list_copy[idx-1]
                operand2 = ex_list_copy[idx+1]
                if i == '+':
                    calc_result = operand1 + operand2
                elif i == '-':
                    calc_result = operand1 - operand2
                elif i == '*':

                    calc_result = operand1 * operand2

                del ex_list_copy[idx - 1]
                del ex_list_copy[idx - 1]
                del ex_list_copy[idx - 1]
                ex_list_copy.insert(idx - 1, calc_result)

        if ex_list_copy[0] < 0:
            answer.append(-1*ex_list_copy[0])
        else:
            answer.append(ex_list_copy[0])

    return max(answer)

if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression))