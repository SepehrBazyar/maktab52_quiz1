import sys

def swap_case(functions):
    def wrapper(*args, **kwargs):
        return functions(*args,**kwargs).swapcase()
    return wrapper

def duplicate(path: str) -> str:
    with open(path) as fl:
        lines = fl.readlines()
    for line in lines:
        words = line.strip().split(' ')
        for word in words:
            if not len(word) == len(set(word)):
                yield word

for item in duplicate('test.txt'):
    print(item)
