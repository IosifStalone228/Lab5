from random import randint


def get_unique_list_numbers(beggining, end) -> list[int]:
    list_ = []
    for i in range(1, 16):
        a = randint(beggining, end + 1)
        if a in list_:
            a = randint(beggining, end + 1)
            list_.append(a)
        else:
            list_.append(a)
    return list_


list_unique_numbers = get_unique_list_numbers(-10, 10)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
