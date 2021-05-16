import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub("[^a-z0-9._-]+","",new_id)
    new_id = re.sub("[.]{2,}", ".", new_id)


    if new_id.startswith(".") :
        new_id = new_id[1:]
    if new_id.endswith(".") :
        new_id = new_id[:-1]

    if not new_id :
        new_id = "a"

    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id.endswith("."):
            new_id = new_id[0:14]

    newidlen = len(new_id)

    if newidlen <=2:
        banbok = 3-newidlen
        mychar = new_id[newidlen-1:]
        new_id = new_id + (mychar*banbok)

    return new_id


if __name__ == "__main__":
    new_id = "abcdefghijklmn.p"
    print(solution(new_id))