def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            return participant[i]


    return participant[len(participant)-1]

if __name__ == '__main__':
    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]
    print(solution(participant, completion))


