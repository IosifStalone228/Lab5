from random import sample


def get_random_password(n=8) -> str:
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = "abcdefghijklmnopqrstuvwxyz"
    c = "0123456789"
    listup = list(a)
    listdown = list(b)
    listnum = list(c)
    listnum.extend(listup)
    listnum.extend(listdown)
    password = sample(listnum, n)
    return password


print(get_random_password())
