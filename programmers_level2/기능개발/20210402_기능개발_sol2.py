import math

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
       # print("iter!!!")
       # print("")
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):

            #print("Q[-1][0]",Q[-1][0])
            #print("-((p-100)//s)",-((p-100)//s))
            Q.append([-((p-100)//s),1])
            #print("Q",Q)
        else:
            #print("else!!!-((p-100)//s)",-((p-100)//s))
            #print("Q[-1][1]",Q[-1][1])
            Q[-1][1]+=1
    return [q[1] for q in Q]


if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))