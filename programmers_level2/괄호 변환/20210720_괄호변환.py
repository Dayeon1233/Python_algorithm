from collections import deque
def solution(p):
    if not p:
        return p
    if check_u_right(p):
        return p
    else:
        idx = seperate(p)

        u = p[:idx]
        v = p[idx:]
        if check_u_right(u):
            return u + solution(v)
        else:

            return make_right(u,v)


def seperate(p):
    st = deque()

    length = len(p)
    for i in range(0,length):
        if i > 0 and not st:
            return i

        if p[i] == '(' and st:
            if st[-1] == ')':
                st.pop()
        elif p[i] == ')' and st:
            if st[-1] == '(':
                st.pop()
            else :
                st.append(')')
        else:
            st.append(p[i])
    return length

def check_u_right(u):
    st = deque()
    for ch in u:
        if ch == '(':
            st.append(ch)
        elif ch == ')' and st:
            if st[-1] == '(':
                st.pop()

    if st :
        return False
    else:
        return True


def make_right(u,v):
    v=solution(v)
    if v:
        temp = '(' + v + ')'
    else:
        temp = '()'

    u=u[1:-1]
    for ch in u:
        if ch == '(':
            temp += ')'
        elif ch == ')':
            temp += '('
    return temp


if __name__ == "__main__":
    p= ''
    print(solution(p))