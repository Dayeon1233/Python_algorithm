def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]


if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands =  [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, commands))


