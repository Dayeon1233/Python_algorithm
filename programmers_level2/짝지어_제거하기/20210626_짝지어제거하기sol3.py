from collections import deque

def solution(s):#baabaa
    st = deque()
    for i in s:
        if st:
            #tmp = st.pop()
            if i == st[-1]:
                st.pop()
            else:
                st.append(i)
        else :
            st.append(i)
    if st:
        return 0
    else:
        return 1




if __name__ == "__main__":

    s="baabaa"

    print(solution(s))