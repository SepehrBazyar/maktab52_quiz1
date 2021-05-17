import sys

def swap_case(gen):
    def wrapper(*args, **kwargs):
        output = []
        for item in gen(*args, **kwargs):
            output.append(item.swapcase())
            yield output[-1]
    return wrapper

@swap_case
def duplicate_gen(path: str) -> str:
    with open(path) as fl:
        lines = fl.readlines()
    for line in lines:
        words = line.strip().split(' ')
        for word in words:
            if not len(word) == len(set(word)):
                yield word

for item in duplicate_gen(sys.argv[1]):
    print(item)
