import sys

def swap_case(functions):
    def wrapper(*args, **kwargs):
        answer = functions(*args,**kwargs)
        output = []
        for item in answer:
            output.append(item.swapcase())
        return output
    return wrapper

def duplicate_gen(path: str) -> str:
    with open(path) as fl:
        lines = fl.readlines()
    for line in lines:
        words = line.strip().split(' ')
        for word in words:
            if not len(word) == len(set(word)):
                yield word

@swap_case
def duplicate_fun(path: str) -> list:
    words = [word for word in duplicate_gen(path)]
    return words

for item in duplicate_fun(sys.argv[1]):
    print(item)

