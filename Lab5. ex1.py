# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint


def finding(beggining, end):
    list_ = []
    for num in range(beggining, end+1):
        dictionary = {}
        dictionary['bin'] = bin(num)
        dictionary['dec'] = num
        dictionary['hex'] = hex(num)
        dictionary['oct'] = oct(num)
        list_.append(dictionary)
    return list_


pprint(finding(0, 15))