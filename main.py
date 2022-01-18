import sys


def func(a, b):
    return a + b


if __name__ == '__main__':
    args = sys.argv
    if len(args) >= 2:
        print(f"a={argv[1]}")
        print(f"b={argv[2]}")
        c = func(x,b)
        print(f"add(a,b)={c}")
    else:
        print("usage: cmd a b")
